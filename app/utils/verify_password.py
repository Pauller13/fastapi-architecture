from utils.config import pwd_context


# === Fonction pour vérifier un mot de passe ===
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
