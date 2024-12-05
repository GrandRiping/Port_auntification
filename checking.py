import bcrypt

def checking_password(entred,hashed):
    """
    Проверка хэша введённого пароля и пароля из БД
    Получает на вход пароль при попытке входа и хэш соотвествующего пароля из БД
    Возвращает True/False в зависимотси от того, совпали проверяемые пароли или нет
    """
    entred=entred.encode('utf-8')
    if isinstance(hashed, str):
        hashed= hashed.encode('utf-8')
    return bcrypt.checkpw(entred,hashed)