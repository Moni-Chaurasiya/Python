from passlib.context import CryptContext
from datetime import timedelta, datetime
import jwt
from src.config import Config
import uuid
import logging
password_context = CryptContext(
    schemes=["bcrypt"],
    # additional schemes (argon2, pbkdf2_sha256) can be added if desired
)
ACCESS_TOKEN_EXPIRY=30000
# bcrypt limits input to 72 bytes.  If a longer password is passed to
# passlib it raises MissingBackendError/ValueError; bcrypt itself silently
# truncates.  We'll proactively truncate to avoid the exception and to make
# hashing deterministic.
 
def generate_password_hash(password: str) -> str:
    pw_bytes = password.encode("utf-8")
    if len(pw_bytes) > 72:
        # cut off at 72 bytes, dropping any partial utf-8 sequence at end
        password = pw_bytes[:72].decode("utf-8", errors="ignore")
    return password_context.hash(password)

def verify_password(password:str,hash:str)->bool:
    return password_context.verify(password,hash)

def create_access_token(user_data:dict,expiry:timedelta=None, refresh:bool=False):
    payload={}
    payload['user']= user_data
    # expiration should be a point in time, not a timedelta object.
    # if an explicit expiry timedelta is provided, add it to now;
    # otherwise use the default ACCESS_TOKEN_EXPIRY seconds.
    exp_time = datetime.now() + (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY))
    # JWT libraries typically accept datetime objects and will convert them
    # to numeric timestamps internally. We can also pass an int timestamp
    # for clarity.
    payload['exp'] = exp_time
    payload['jti']= str(uuid.uuid4())
    
    token= jwt.encode(
        payload=payload,
        key= Config.JWT_SECRET,
        algorithm=Config.JWT_ALGORITHM
    )
    return token

def decode_token(token:str)->dict:
 try:
    token_data=jwt.decode(
        jwt=token,
        key=Config.JWT_SECRET,
        algorithms=[Config.JWT_ALGORITHM]
    )
    return token_data
 except jwt.PyJWKError as e:
     logging.exception(e)
     return None
     