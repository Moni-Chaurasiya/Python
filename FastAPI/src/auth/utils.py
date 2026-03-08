from passlib.context import CryptContext

password_context = CryptContext(
    schemes=["bcrypt"],
    # additional schemes (argon2, pbkdf2_sha256) can be added if desired
)

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