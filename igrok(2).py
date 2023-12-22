from random import choice



def get_hero(
    name=None,
    hp=100, 
    level=1, 
    xp=0, 
    money=25,
    inventory=None
    ) -> list:
    ''' Возвращает список - героя с 6 характеристиками'''
    if not name:
        name = choice(['Адольф', 'Иосиф', 'Владимир', 'Мао'])
    if not inventory:   
        inventory = []
    return [name, hp, level, xp, money, inventory]


def show_hero(hero: list) -> None:
    ''' Выводит на экран все 6 характеристик героя '''
    print('-----------------------------')
    print('имя:', hero[0])
    print('здоровье:', hero[1])
    print('уровень:', hero[2])
    print('опыт:', hero[3])
    print('деньги:', hero[4])
    print('инвентарь:', hero[5])
    print('-----------------------------')


def visit_stall(hero: list, stall_items: list):
    ''' 
    Выводит на экран текст ларька
    ВЫВОДИТ НА ЭКРАН ОПЦИИ
    Предлагает герою выбор одной из опций
    Работает по выбраной опции

    '''
    show_hero(hero)
    print(f'{hero[0]} приехал в ларек ')
    print('РАСПРОДАЖА ДО 26 ДЕКАБРЯ, ВСЕ ТОВАРЫ ПО 10 РУБЛЕЙ')
    price_tmp = 10
    print('1 - купить товары')
    print('2 - продать товары')
    print('0 - уйти')
    option = input('Введите номер функции_ ')
    if option == '1':
        for num, item in enumerate(stall_items, 1):
            print(f'{num} - {item}')
        print('0 - Отмена')
        option = input('Введите номер функции для покупки_ ')
        if int(option) < 0 or int(option) > len(stall_items):
            print('неверная опция')
        elif option == '0':
            print('выход из покупок')
        else:
            if hero[4] < price_tmp:
                print(f'y {hero[0]} неедостаточно денег')
            else:
                hero[4] -= price_tmp
                item_index = int(option) - 1
                item_name = stall_items[item_index]
                print('-----------------------------')
                print(f'{hero[0]} купил {item_name}')
                print('-----------------------------')
                hero[5].append(stall_items.pop(item_index))
                show_hero(player)
   



player = get_hero('Вася')
stall_items = ['зелье лечения', 'зелье опыта', 'кот в мешке']
visit_stall(player, stall_items)
visit_stall(player, stall_items)