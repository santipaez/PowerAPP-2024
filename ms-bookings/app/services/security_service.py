from werkzeug.security import generate_password_hash, check_password_hash

class SecurityService:

    @staticmethod
    def generate_hash(password: str) -> str:
        return generate_password_hash(password)
    
    @staticmethod
    def check_password(password: str, hash: str) -> bool:
        return check_password_hash(hash, password)