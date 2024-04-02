'''
класс это идея (пример:
подорили ребенку чертеж велосипеда,
на черчеже нельзя ехать, это класс)
'''


class Player:
    ''' Игрок '''
    def __init__(self, name: str, hp: int, power: int) -> None:
        '''конструктор классa'''
        self.name = name
        self.hp = hp
        self.power = power

    def __str__(self) -> str:
        return f'Игрок {self.name}, жизни: {self.hp}'
    
    def attack(self, enemy):
        enemy.hp -= self.power
        print(self.name, 'атаковал', enemy.name)
        print(self.player)
    

class Game:
    def __init__(self) -> None:
        self.player = Player('Вася', 100, 3)
        self.enemy = Player('Куан Чи', 90, 5)
        self.fight()
    
    def fight(self) -> None:
        while True:
            self.player.attack(self.enemy)
            print(self.player)
            self.enemy.attack(self.player)
            print(self.enemy)
            # TODO завершить бой и опредилить победителя


p_1 = Player('Вася', 100, 3)
p_2 = Player('Ася', 90, 5)
print(p_1)
print(p_2)


Game()