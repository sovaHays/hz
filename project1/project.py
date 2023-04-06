from pygame import *
import sys

font.init()


def showEndWindow(window, message):
    clock = time.Clock()
    run = True
    font.init()
    text = font.Font(None, 70).render(message, True, (255, 255, 255))
    while run:
        for e in event.get():
            if e.type == QUIT:
                quit()

        window.blit(text, (250, 250))
        display.update()
        clock.tick(60)


size = (1400, 1000)
window = display.set_mode(size)
window.fill((255, 0, 0))

game = True

clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__()
        self.speed = speed
        self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed


class Fruit(GameSprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__(player_image, x, y, speed, size_w, size_h)
        self.hide = None


player = Player("player.png", 0, 790, 6, 205, 224)
fruit = Fruit("fruit-apple.png", 300, 300, 3, 128, 128)

fruits = []
score = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
            game = False

    if player.rect.x < 0:
        player.rect.x = 0

    if player.rect.x > 1200:
        player.rect.x = 1200

    if player.rect.colliderect(fruit.rect):
        score += 1

    fruit.rect.y += fruit.speed

    player.update()
    fruit.update()

    player.draw(window)
    fruit.draw(window)

    display.update()
    window.fill((0, 0, 0))

    clock.tick(60)

    f1 = font.Font(None, 36)
    text1 = f1.render(str(score), True, (180, 0, 0))
    window.blit(text1, (10, 50))
quit()
