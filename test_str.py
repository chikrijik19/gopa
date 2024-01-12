'''
опредилить функциюб которая возвращает True,
если пароль подходящий, иначе False
Правельный пароль:
    от 10 символов
    содержит заглавные буквы
    содержит строчные буквы
    содержит цифры
'''
def password_scanner(password: str) -> bool:
    if len(password) < 10:
        return False
    elif password.isupper():
        return False
    elif password.islower():
        return False
    elif password.isdigit():
        return False
    else:
        return True



password = input('Введите пароль: ')
printer = password_scanner(password)
print(printer)