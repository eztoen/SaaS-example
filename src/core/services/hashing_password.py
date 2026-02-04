from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')

def get_psw_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_psw(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)