from users import adding, hashed_password, checking_login
from hashing import hashing_password
from checking import checking_password
from termcolor import colored
            
def menu():
    """
    Главное меню
    """
    print(f'1.- Регистрация\n2.- Вход\n3.- Выход')

def register():
    """
    Регистрация нового пользователя с занесением данных в БД
    При удачной регистрации возвращает логин и хэш соответствующего пароля
    """
    username=str(input('Придумайте логин '))
    if checking_login(username):
        print(colored('Этот логин уже занят','red'))
        return
    user_password=str(input('Придумайте пароль '))
    conf_password=str(input('Подвтерждение '))
    if user_password!=conf_password:
        print(colored('Пароли не совпадают, попробуйте ещё раз','red'))
        return
    hashed=hashing_password(user_password)
    adding(username,hashed)
    print(colored('Регистрация прошла успешно','green'))

def auntification():
    """
    Сверка введённых данных с данными из БД
    Возвращает False в случае ввода неверного логина или логин и пароль для последующей проверки с хэшом из БД
    """
    username=str(input('Введите логин '))
    if not checking_login(username):
        print(colored('Неверный логин, зарегистрируйтесь','red'))
        return False
    user_password=str(input('Введите пароль '))
    return username,user_password


while True:
    menu()
    act=int(input())
    if act== 1:
        print('Регистрация')
        register()
    elif act== 2:
        print('Вход')
        res= auntification()
        if res:
            login=str(res[0])
            password=str(res[1])
            if checking_login(login):
                hashed=hashed_password(login)
                if checking_password(password,hashed):
                    print(colored(f'Добро пожаловать, {login}!','cyan'))
                else:
                    print(colored("Неверный пароль",'red'))
    elif act==3:
        print('Выход')
        break
    else:
        print(colored('Некорректный ввод','red'))
