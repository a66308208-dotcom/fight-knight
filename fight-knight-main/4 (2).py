from pygame import *
mixer.init()
mixer.music.load('1-03_-subwoofer-lullaby.mp3')
mixer.music.play()



# Настройки окна
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
back = (200, 255, 255)

# Инициализация шрифта
font.init()
font = font.Font(None, 35)

lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

clock = time.Clock()
FPS = 60

# Класс для ракетки
class Player:
    def __init__(self, color, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.color = color

    def draw(self):
        draw.rect(window, self.color, self.rect)

    
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.alive = True
    def draw(self):
        draw.rect(window, self.color, self.rect)

    def take_damage(self, Player)
        actual_damage = max(1, Playe)
        self.hp-= actual_damage
        print(f'{self.name} получает {actual_damage} урона!')
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            print(f'{self.name}убит!')
        return actual_damage
    def heal(self):
        heal_amount = random.randint(15, 30)
        self.hp = min(self.max_hp, self.hp + heal_amount)
        print(f'{self.name} восстановил {heal_amount} HP! текущее HP: {self.hp}')

    def is_alive(self):
        return self.alive    
# Создаем объекты
racket1 = Player((0, 0, 255), 30, 200, 80, 80)
racket1_damager = Player((0, 0, 255), 30, 200, 150, 20)
racket2 = Player((30, 148, 255), 550, 200, 80, 80)
racket2_damager = Player((30, 148, 255), 500, 200, 150, 20)


# Основной цикл
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(back)

    # Рисуем объекты
    racket1.draw()
    racket2.draw()
    racket1_damager.draw()
    racket2_damager.draw()
    

    display.update()
    clock.tick(FPS)

