from random import shuffle
from os import system

'''
Карта
{
    'цена': 10,
    'масть': 'пик',
    'название': '10'
}

Масти:
    черви, пики, бубны, крести

Колода:
    на каждую масть карты от 6 до туза = 36 карт

Игроки
    от 2 до ...

Перетасовать колоду

Каждому игроку даем по 2 карты

Можно смотреть только свои карты

Ход
    беру еще карту (сколько угодно, не больше, чем осталось в колоде)
    или закончить ход

Каждый игрок делает 1 ход за партию

Если сумма цен всех карт игрока > 21, то он проиграл

Если все игроки проиграли, то это ничья

Побдитель - тот, кто набрал самую большую сумму цен своих карт
'''


def get_deck() -> list[dict]:
    '''Возвращает колоду карт'''
    suits = ('черви', 'пики', 'бубны', 'крести')
    cards = {
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'валет': 2,
        'дама': 3,
        'король': 4,
        'туз': 11
    }
    deck = [] # колода
    for suit in suits:
        for item in cards:
            card = {
                'цена': cards[item],
                'масть': suit,
                'название': item
            }
            deck.append(card)
    return deck


def get_players() -> list[dict]:
    '''Возвращает список игроков'''
    player_1 = {
        'имя': 'Вася',
        'карты': [],
        'человек': False,
        'сумма': 0,
        'предел': 17
    }
    player_2 = {
        'имя': 'Яблоко',
        'карты': [],
        'человек': False,
        'сумма': 0,
        'предел': 16
    }
    return [player_1, player_2]


def deal_cards(num: int) -> None:
    '''Раздает кажому игроку по 2 карты'''
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop())


def show_cards() -> None:
    for card in player['карты']:
        print(card['название'], card['масть'])


def calculate_total_values(player: dict) -> None:
    total = 0
    for card in player['карты']:
        total += card['цена']
    player['сумма'] = total


def show_statistics():
    for player in players:
        if player['сумма'] > 21:
            print(player['имя'], 'набрал', player['сумма'], 'очков......перебор!')
        else:
            print(player['имя'], 'набрал', player['сумма'], 'очков')


def show_result() -> str:
    totle_values = [player['сумма'] for player in players]
    
    if totle_values.count(totle_values[0]) == len(totle_values):
        print('Ничья') # у всех одинаковое кол-во очков
        return 'Ничья'
    else:
        totle_values = [player['сумма'] for player in players if player['сумма'] < 22]
        for player in players:
            if player['сумма'] == max(totle_values):
                print('Победил', player['имя'])
                return player['имя']

statistics = dict()

for i in range(107):
    deck = get_deck()
    shuffle(deck)
    players = get_players()
    cards_per_turn = len(deck) // len(players)
    deal_cards(2)

    for player in players:
        while True:
            system('cls')
            show_cards()
            calculate_total_values(player)
            print('сумма очков:', player['сумма'])
            if player['человек']:
                player_option = input('Взять карту из колоды (y/n)? ')
            else:
                if player['сумма'] < 17:
                    player_option = 'y'
                else:
                    player_option = 'n'
            if player_option.lower() == 'y':
                if len(player['карты']) < cards_per_turn:
                    player['карты'].append(deck.pop())
                else:
                    print('Невозможно взять ещё карту!')
                    break
            else:
                break
    


system('cls')
# show_statistics()
winner = show_result()

'''
написать на перерыве маме что бы написала заявление об переходе в другую групу
'''
if winner not in statistics:
    statistics[winner] = 1
else:
    statistics[winner] += 1

print(statistics)
