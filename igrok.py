from random import randint



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
        names = ('Адольф', 'Иосиф', 'Владимир', 'Мао')
        name = names[randint(0, len(names) - 1)]
    if not inventory:   
        inventory = []
    return [name, hp, level, xp, money, inventory]


def show_hero(hero: list) -> None:
    ''' Выводит на экран все 6 характеристик героя '''
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
    print('1 - купить товары')
    print('2 - продать товары')
    print('0 - уйти')
    option = input('Введите номер функции_ ')
    if option == '1':
        for num, item in enumerate(stall_items, 1):
            print(f'{num} - {item}')
        option = input('Введите номер функции или введите 0 для отмены_ ')
        # TODO: купить товар по выбранной опции   



player = get_hero('Вася')
stall_items = ['зелье лечения', 'зелье опыта']
visit_stall(player, stall_items)
