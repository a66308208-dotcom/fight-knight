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

# Класс для мяча
class Ball:
    def __init__(self, color, x, y, size):
        self.rect = Rect(x, y, size, size)
        self.color = color

    def draw(self):
        draw.rect(window, self.color, self.rect)

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

