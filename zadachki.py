def get_stason(num) -> list:
    if num == 1 or num == 2 or num == 12:
        print('зима')
    elif num == 3 or num == 4 or num == 5:
        print('весна')
    elif num == 6 or num == 7 or num == 8:
        print('лето')
    elif num == 9 or num == 10 or num == 11:
        print('осень')
    else:
        print('не')


get_stason(12)
