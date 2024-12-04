import bcrypt

def hashing_password(password_from_db):
    """
    Хэширование паролей
    Получает на вход либо созданный сейчас пароль, либо пароль, вводимый при попытке входа
    Возвращает их хэш для последующей проверки или внесения в БД
    """
    salt=bcrypt.gensalt()
    hashed_password=bcrypt.hashpw(password_from_db.encode('utf-8'),salt)
    return hashed_password