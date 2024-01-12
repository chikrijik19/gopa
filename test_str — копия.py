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
    check_1 = False #проверяет пароль на наличее 10 и более букв
    check_2 = False #проверяет пароль на наличее заглавных букв
    check_3 = False #проверяет пароль на наличее строчных букв
    check_4 = False #проверяет пароль на наличие цифр
    if len(password) < 10:
        return False
    else:
        check_1 = True
    if password.isupper():
        return False
    else:
        check_2 = True
    if password.islower():
        return False
    else:
        check_3 = True
    if password.isdigit():
        return False
    else:
        check_4 = True
    if check_1 == True and check_2 == True and check_3 == True and check_4 == True:
        return True
    else:
        return False



password = input('Введите пароль: ')
printer = password_scanner(password)
print(printer)