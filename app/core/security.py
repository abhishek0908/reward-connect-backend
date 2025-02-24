import bcrypt 
import jwt 
import datetime
SECRET_KEY = "abhishek"
def hash_password(password:str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"),salt).decode("utf-8")

def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_jwt_token(data:dict):
    expiration = datetime.datetime.utcnow()+datetime.timedelta(days=1)
    payload = {**data,"exp":expiration}
    return jwt.encode(payload,SECRET_KEY,algorithm="HS256")


# Decode JWT Token
def decode_jwt_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
