'''
Мы делали компьютерного игрока
мы написали что он кидает себе в список пустые клетки 
ЧТО НУЖНО СДЕЛАТЬ:
он должен на пустые клетки ставить себя
'''




'''
1 игрок - X
2 игрок - 0
игровое поле из 9 клеток: 3 на 3
игроки ходят по очереди
сделать ход - поставить Х или 0 в свободную клетку поля
условия победы (достаточно одного):
    3 одинаковых символа по горизонтали в любом ряду
    3 одинаковых символа по вертикали в любой колонне
    3 одинаковых символа по горизонтали в любой из них
если победитель не выявлен, а свободные клетки кончились - ничья
'''

from os import system

# глобальные константы
EMPTY = '.'
PLAYER_1 = 'x'
PLAYER_2 = '0'


def get_field() -> list[str]:
    ''' Возвращает поле из 9 пустых клеток '''
    field = []
    for i in range(9):
        field.append(EMPTY)
    return field


def draw_field(field: list) -> None:
    ''' Выводит на экран игровое поле по 3 клетки в ряд '''
    system('cls')
    for i in range(0, 9, 3):
        print(field[i], field[i + 1], field[i + 2])


def make_move(field: list, player: str, is_auto: bool) -> None:
    '''
    Спрашивает у игрока номер клетки поля
    Проверяет, что клетка с таким номером в пределах поля
    Проверяет, занята ли клетка
    При удачных проверках
    Изменяет клетку под выбранным номером на player - символ игрока
    '''
    if not is_auto:
        while True:
            try:
                cell_num = int(input(f'Введите номер клетки для хода {player}: '))#проверка есть ли клетка
            except ValueError:
                print('Ошибка! Номером клетки должно быть целое число!')
                continue
            if cell_num < 1 or cell_num > 9:
                print('Ошибка! Номер клетки должен быть от 1 до 9 вкл!')
            elif field[cell_num - 1] != EMPTY:
                print('Ошибка! Эта клетка занята!')
            else:
                field[cell_num - 1] = player
                break
    else:
        '''
        собрать пустые клетки в список
        выбрать случайную клетку из списка
        поставить туда игрока
        '''
        empty_cells = []
        for cell in field:
            if cell == EMPTY:
                empty_cells.append(cell)
        



def get_winner(field: list, player: str) -> str: #определяет победителя
    #проверка горизонтали
    for i in range(0, 7, 3):
        if field[i] == field[i + 1] == field[i + 2] == player:
            return player

    #проверка ветертекали
    for i in range(3):
        if field[i] == field[i + 3] == field[i + 6] == player:
            return player
    
    #проверка наискосок
    if field[0] == field[4] == field[8] == player:
        return player

    if field[2] == field[4] == field[6] == player:
        return player
    


def main() -> None:
    '''
    Создает поле
    Начинает игру с 1-го хода
    Пока не будет победителя или есть свободные клетки,
    игроки ходя по очереди
    '''
    field = get_field()
    moves = 1
    while moves <= 9:
        draw_field(field)
        if moves % 2: #проверка четного хода
            player = PLAYER_1
            is_auto = False
        else:
            player = PLAYER_2
            is_auto = True
        make_move(field, player, is_auto)
        moves += 1
        winner = get_winner(field, player)
        if winner:
            draw_field(field)
            print('победил', player)
            break
    else:  # сработает, если не было break
        draw_field(field)
        print('Игра окончена! Ничья!') 



main()
