import bcrypt

def hashing_password(password_from_db):
    """
    Хэширование паролей
    Получает на вход созданный при регистрации пароль
    Возвращает его хэш
    """
    salt=bcrypt.gensalt()
    hashed_password=bcrypt.hashpw(password_from_db.encode('utf-8'),salt)
    return hashed_password