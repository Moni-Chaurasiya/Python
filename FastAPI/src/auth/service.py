from .models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from .schema import UserCreateModel
from .utils import generate_password_hash 
from sqlmodel import select
class UserService:
    async def get_user_by_email(self, email:str,session:AsyncSession):
        statement = select(User).where(User.email==email)
        
        result = await session.exec(statement)
        
        user = result.first()
        return user
    
    async def user_exists(self, email,session:AsyncSession):
        # call the helper above correctly, self will be implicitly passed
        user = await self.get_user_by_email(email,session)
        return True if user is not None else False
        # if user is None:
        #     return False
        # else: return True
    
    async def create_user(self,user_data:UserCreateModel,session:AsyncSession):
        user_data_dict = user_data.model_dump() 
        new_user = User(
            **user_data_dict
        )
        try:
            new_user.password_hash = generate_password_hash(user_data_dict['password'])
            new_user.role = "user"
        except Exception as exc:
            # if hashing fails for some reason, bubble as a 400
            from fastapi import HTTPException, status
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"password hashing failed: {exc}"
            )
        session.add(new_user)
        await session.commit()
        # refresh so that defaults (created_at/updated_at, uid) are loaded
        await session.refresh(new_user)
        return new_user