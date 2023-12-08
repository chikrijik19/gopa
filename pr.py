from random import randint

name_level = 1
name_hp = name_level + 10
name_foce = randint(1, 5) * name_level
name_money = 10

enemy_level = 1
enemy_hp = enemy_level + 15
enemy_foce = randint(2, 7) * enemy_level

right_run = 0
left_run = 0
center_run = 0

name_frend = 'нету'

def right():
    print('там', name, 'ждал человек, он случайно там стоял но не суть')
    print('чел:')
    frend = input('будешь дружить? ')
    if frend == 'да':
        print('чел:')
        print('я чел')
        right_run = 1
        name_frend = 'да'
    elif frend == 'нет':
        print('чел:')
        print('ну ок')
        right_run = 1
        name_frend = 'нету'
    else:
        print('что?')



def left(): 
    print('гопникии:')
    print('слышь бабки гони а то в деревянном ящике под землёй окажешься')
    choise = input('воу, ситуация не очень, если идти в бой, то нажми 1, если хочешь предложить им в кости, то нажми 2 ')
    if choise =='1':
        fight(name)
    elif choise == '2':
        dice(name, name_money, enemy_name='гопники')            



def center():
    print('опа деньги')
    name_money = (name_money + 5)



def question():
    run = input('куда пойдёшь? ')
    if run == 'направо':
        right()
    elif run == 'налево':
        left()
    elif run == 'прямо':
        center()
    else:
        print('что?')
    



def stall():
    product = input('здравствуй, я богатый чел, если хочешь купить нож от гопников за 5 долларов, то нажми 1, если хочешь купить подорожник дающий полное здаровье за 3 доллара, то нажми 2, если хочешь уйти то нажми 0')
    if product == 1:
        if name_money < 5:
            name_foce = randint(5, 10)
            print('теперь не бойся гопников, твоя сила', name_foce)
        else:
            print('прости, но тебе не хватает')
    elif product == 2:
        if name_money < 3:
            name_hp = name_level + 10
            print('ты полностью излечился, твоё здоровье', name_hp)
    elif product == 0:
        print('ну пока')
    else:
        print('немного не понял, повтори')



def fight(
        name,
        name_level=1,
        name_hp=1 + name_level,
        name_foce=randint(1, 5) * name_level,
        enemy_name='гопники',
        enemy_hp=12 + enemy_level,
        enemy_level=1,
        enemy_foce=randint(2, 7) * enemy_level
):
        print('БОЙ НАЧИНАЕТСЯ!')
        while True:
            player_attak = name_foce
            input('-------нажмите Enter что бы бить-------')
            enemy_hp -= player_attak
            print(name, 'ударил', enemy_name, 'на', player_attak, 'hp')
            print('y', enemy_name, 'осталось', enemy_hp, 'жизней')
            if name_hp <= 0:
                print(name, 'проиграл')
                break

            enemy_attak = enemy_foce
            name_hp -= enemy_attak
            print(enemy_name, 'ударил', name, 'на', enemy_attak, 'hp')
            print('y', name, 'осталось', name_hp, 'жизней')
            if enemy_hp <= 0:
                print(enemy_name, 'проиграл')
                break



def dice(name, name_money, enemy_name='гопники'):
    print('гопники:')
    print('нуу, так тоже можно')
    if name_money >= 1:
        print('ИГРА НАЧАЛАСЬ!')
        print('__________________________________')
        print('y', name, name_money, 'денег')
        bet = int(input('сколько ставишь? '))
        if bet > name_money:
            print('да нет у тебя столько денег')
        elif bet < 1:
            print('ставь нормальную ставку')
        else:
            print('ставка игрока', bet)
            name_bet = randint(1, 6)
            enemy_bet = randint(1, 6)
            if name_bet > enemy_bet:
                name_money += bet * 2
                print('число', name, name_bet, 'число', enemy_name, enemy_bet)
                print(name, 'выиграл', bet * 2, 'долларов')
                print('y', name, name_money, 'долларов')
            elif name_bet == enemy_bet:
                print('ничья')
            else:
                name_money -= bet
                print('число', name, name_bet, 'число', enemy_name, enemy_bet)
                print(name, 'проиграл', bet , 'долларов')
                print('y', name, name_money, 'долларов')
    else:
        print('так стоп, у тебя нет денег клоун')


    
        


name = input('кто ты воин? ')
print(name, 'шёл по улице и нашел указатель: направо пойдёшь - друга верного найдёшь, налево пойдёшь - на гопников наткнёшся, а прямо пойдёшь - 5 долларов получешь')
run = input('куда пойдёшь? ')
if run == 'направо':
    right()
elif run == 'налево':
    left()
elif run == 'прямо':
    center()
else:
    print('что?')

question()
question()