frend = 'нету'
r_right = False
r_left = False
r_center = False

def right():
    print('там', name, 'ждал человек, он случайно там стоял но не суть')
    print('чел:')
    frend = input('будешь дружить? ')
    if frend == 'да':
        print('чел:')
        print('я чел')
    elif frend == 'нет':
        print('чел:')
        print('ну ок')
    else:
        print('что?')



def left():
    print('гопникии:')
    print('слышь бабки гони а то в деревянном ящике под землёй окажешься')



def center():
    print('опа деньги')



def question():
    run = input('куда пойдёшь? ')



def stall():
    product = input('здравствуй, я богатый чел, если хочешь купить нож от гопников за 5 долларов, то нажми 1, если хочешь купить подорожник дающий полное здаровье за 3 доллара, то нажми 2, если хочешь уйти то нажми 0')


name = input('кто ты воин? ')
print(name, 'шёл по улице и нашел указатель: направо пойдёшь - друга верного найдёшь, налево пойдёшь - на гопников наткнёшся, а прямо пойдёшь - 5 долларов получешь')
while r_right == False or
run = input('куда пойдёшь? ')
if run == 'направо':
    right()
elif run == 'налево':
    left()
elif run == 'прямо':
    center()
else:
    print('что?')

