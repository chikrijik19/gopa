import os

'''
Класс Weapon
Дать каждому игроку оружие
Это оружие должно участовать в расчете атаки
'''


class Weapon:
    '''Оружие'''
    def __init__(self, name: str, attack_power: int) -> None:
        self.name = name
        self.attack_power = attack_power

    def __str__(self) -> str:
        return f'{self.name} ({self.attack_power})'


class Player:
    '''Игрок'''
    def __init__(self, name: str, hp: int, weapon=None, level = 1, xp = 0) -> None:
        self.name = name
        self.hp = hp
        self.power = 1
        self.default.weapon = Weapon('Кулаки', 1)
        if weapon:
            self.weapon = weapon
        else:
            self.weapon = self.default.weapon
        self.level = level
        self.xp = xp

    def show(self) -> None:
        '''Строковое представление экземплра'''
        print(self.name.center(20, '-'))
        print('уровень:', self.level)
        print('опыт:', self.xp)
        print('жизни:', self.hp)
        print('сила:', self.power)
        print('оружие', self.weapon)
        print('-' * 20)

    def attack(self, enemy) -> None:
        '''Игрок атакует противника'''
        if self.hp <= 0:
            return
        damage = self.power + self.weapon.attack_power
        enemy.hp -= damage
        print(self.name, 'атаковал', enemy.name)
    
    def get_award(self, enemy) -> None:
        os.system('cls')
        self.xp += enemy.level
        if self.xp > 9:
            num = self.xp // 10
            for i in num:
                self.xp -= 10
                self.level += 1
        self.show
        print(self.name, 'победил')
        print(self.name, 'получил', enemy.level, 'опыта')


class Game:
    '''Игра'''
    def __init__(self) -> None:
        self.player = Player('Вася', 100, Weapon('Меч Кладенец', 5))
        self.enemy = Player('Упырь', 100)
        self.is_running = False
        self.fight()

    def fight(self) -> None:
        '''Сражение'''
        self.is_running = True
        while self.is_running:
            os.system('cls')
            self.player.show()
            self.player.attack(self.enemy)
            self.enemy.show
            self.enemy.attack(self.player)
            self.check_winner()
            input('ENTER ')
        

    def check_winner(self) -> None:
        ''' Заканчивает игру победой игрока или противника'''
        if self.player.hp <= 0:
            self.is_running = False
        elif self.enemy.hp <= 0:
            self.is_running = False
            self.get_award(self, enemy)


Game()