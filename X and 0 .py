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

from random import choice

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


def make_move(field: list, player: str, is_auto: bool, is_center: bool, is_corner: bool) -> None:
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
        собрать индоксы пустых клеток в список
        выбрать случайную клетку из списка
        поставить туда игрока
        TODO: научить автомат занимать углы
        '''
        empty_cells_indexes = []
        for index in range(9):
            if field[index] == EMPTY:
                empty_cells_indexes.append(index)
        if is_center:
            if 4 in empty_cells_indexes:
                field[4] = player
                return
            
        random_index = choice(empty_cells_indexes)
        field[random_index] = player

        



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
    


def play_game(is_silent: bool) -> str:
    '''
    Создает поле
    Начинает игру с 1-го хода
    Пока не будет победителя или есть свободные клетки,
    игроки ходя по очереди
    '''
    field = get_field()
    moves = 1
    while True:
        if moves > 9:
            winner = 'ничья'
            break
        if not is_silent:
            draw_field(field)
        if moves % 2:  # проверка четного хода
            player = PLAYER_1
            is_auto = True
            is_center = False
            is_corner = False
        else:
            player = PLAYER_2
            is_auto = True
            is_center = True
            is_corner = True
        make_move(field, player, is_auto, is_center, is_corner)
        moves += 1
        winner = get_winner(field, player)
        if winner:
            if not is_silent:
                draw_field(field)
            print('победил', player)
            break
    if not is_silent:
        draw_field(field)
        print('Игра окончена! Результат', winner)

    return winner


winners = [0, 0, 0]  # Х, 0, Ничья
for i in range(1000):
    winner = play_game(True)
    if winner == PLAYER_1:
        winners[0] += 1
    elif winner == PLAYER_2:
        winners[1] += 1
    else:
        winners[2] += 1

print(f'{PLAYER_1} победил {winners[0]} раз')
print(f'{PLAYER_2} победил {winners[1]} раз')
print(f'Ничьих {winners[2]}')
