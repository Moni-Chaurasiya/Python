from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()  

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET : str
    JWT_ALGORITHM: str
    REDIS_HOST:str="localhost"
    REDIS_PORT:int=6379
    
    MAIL_USERNAME:str
    MAIL_PASSWORD :str
    MAIL_FROM:str
    MAIL_PORT:int
    MAIL_SERVER: str
    MAIL_FROM_NAME :str
    MAIL_STARTTLS:bool = True
    MAIL_SSL_TLS:bool = False
    USE_CREDENTIALS:bool= True
    VALIDATE_CERTS:bool = True
    DOMAIN:str
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

Config = Settings()

# TEMP DEBUG (remove later)
print("DATABASE_URL from config =", Config.DATABASE_URL)
