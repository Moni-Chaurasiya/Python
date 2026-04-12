# Import HTTPBearer class from FastAPI's security module.
# HTTPBearer is a base class for handling Bearer token authentication in HTTP requests.
# It automatically extracts the Bearer token from the Authorization header.
from fastapi.security import HTTPBearer

# Import Request class and status constants from FastAPI.
# Request represents an incoming HTTP request, allowing access to headers, body, etc.
# status provides HTTP status code constants (e.g., HTTP_403_FORBIDDEN) for readable error responses.
from fastapi import Depends, Request, status

# Import HTTPAuthorizationCredentials from FastAPI's security.http module.
# This is a Pydantic model that holds the authentication scheme (e.g., "Bearer") and credentials (the token string).
# It's returned by HTTPBearer's __call__ method after extracting from the header.
from fastapi.security.http import HTTPAuthorizationCredentials

# Import decode_token function from the local utils module (in the same auth package).
# decode_token is a custom utility function that decodes and validates a JWT token.
# It returns the token's payload (e.g., user data, expiration) if valid, or None if invalid/expired.
from .utils import decode_token

# Import HTTPException from FastAPI's exceptions module.
# HTTPException is used to raise HTTP errors with custom status codes and details.
# FastAPI automatically converts these to JSON error responses.
from fastapi.exceptions import HTTPException
from src.db.redis import token_in_blocklist
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .service import UserService
from typing import List, Any
from src.auth.models import User
user_service=UserService()

# Define a custom class AccessTokenBearer that inherits from HTTPBearer.
# This extends the base class to add custom logic for validating access tokens (e.g., checking validity and type).
# It acts as a dependency in FastAPI routes to enforce authentication.
class TokenBearer(HTTPBearer):

    # Define the __init__ method (constructor) for the class.
    # It takes an optional parameter auto_error (default True), which controls whether to raise an error if no token is provided.
    # auto_error=True means HTTPBearer will automatically raise an exception for missing tokens.
    def __init__(self, auto_error=True):
        # Call the parent class's __init__ method with the auto_error parameter.
        # This initializes the base HTTPBearer functionality.
        super().__init__(auto_error=auto_error)

    # Define the __call__ method, which is an async coroutine (due to 'async def').
    # This method overrides the parent's __call__ to customize token processing.
    # It takes a Request object (the incoming HTTP request) and returns HTTPAuthorizationCredentials or None.
    # The '->' indicates the return type annotation (union of credentials or None).
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        # Call the parent class's __call__ method to extract credentials from the request.
        # This returns an HTTPAuthorizationCredentials object containing scheme and credentials.
        # 'await' is used because the parent's method is async.
        creds = await super().__call__(request)

        # Print the scheme (e.g., "Bearer") from the credentials for debugging purposes.
        # This helps verify what authentication scheme is being used.
        print(creds.scheme)

        # Print the credentials (the token string) for debugging.
        # Note: In production, avoid printing sensitive data like tokens; use logging instead.
        print(creds.credentials)

        # Extract the token string from the credentials object.
        # creds.credentials holds the actual Bearer token value.
        token = creds.credentials

        # Decode the token using the imported decode_token function.
        # token_data will contain the JWT payload (e.g., user ID, expiration) if valid, or None if invalid.
        token_data = decode_token(token)

        # Check if the token is not valid using the token_valid method (defined below).
        # 'not self.token_valid' means if token_valid returns False, proceed to raise an error.
        # 'self.token_valid' calls the method on the current instance.
        if not self.token_valid(token):
            # Raise an HTTPException with status 403 (Forbidden) and a custom error message.
            # This blocks the request if the token is invalid or expired.
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail={"errror":"This token is invalid or expired",
                "resolution":"Please get new token"})
        if await token_in_blocklist(token_data['jti']):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail={"errror":"This token is invalid or has been revoked",
                "resolution":"Please get new token"}
            )
        self.verify_token_data(token_data)

        # Commented-out line: An alternative return that would return the raw credentials object.
        # Instead, we return the decoded token data (payload) for use in routes (e.g., user info).
        # return creds

        # Return the decoded token data (e.g., user claims like user_id, roles).
        # This provides authenticated user context to the route handler.
        return token_data

    # Define a helper method token_valid to check if a token is valid.
    # It takes a token string and returns a boolean (True if valid, False otherwise).
    # The '-> bool' is a type annotation for the return value.
    def token_valid(self, token: str) -> bool:

        # Decode the token again using decode_token.
        # This re-validates the token (checking signature, expiration, etc.).
        token_data = decode_token(token)

        # If token_data is not None (meaning decoding succeeded), return True (valid).
        # Otherwise, return False (invalid).
        if token_data is not None:
            return True
        else:
            return False
    
    def verify_token_data(self,token_data):
        raise NotImplementedError("Please Override this method in child classes")
        
class AccessTokenBearer(TokenBearer):
    def verify_token_data(self,token_data:dict)->None:
        # Check if the decoded token data contains a 'refresh' key set to True.
        # This indicates the token is a refresh token, not an access token.
        # Access tokens are for API access; refresh tokens are for obtaining new access tokens.
        if token_data and token_data['refresh']:
            # Raise an HTTPException if a refresh token is provided instead of an access token.
            # This enforces that only access tokens are used for endpoint authentication.
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide an access token"
            )

class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self,token_data:dict)->None:
    
       if token_data and not token_data['refresh']:
     
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide a refresh token"
            )
            
async def get_current_user(
    token_details:dict=Depends(AccessTokenBearer()),
    session:AsyncSession=Depends(get_session)
):
    user_email=token_details["user"]["email"]
    user = await user_service.get_user_by_email(user_email,session)
    return user

class RoleChecker:
    def __init__(self, allowed_roles:List[str]) ->None:
        self.allowed_roles= allowed_roles
        
    def __call__(self, current_user:User = Depends(get_current_user))->Any:
        if current_user.role in self.allowed_roles:     
            return True
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            details= "You are not allowed to perform this action"
        )
        