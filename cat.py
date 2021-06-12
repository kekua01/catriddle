import random
import pygame
import sys
import math

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE
BOX_NUMS = 5
CAT_HIDDEN = True #change this to see or hide the cat
MOVES = [-1, 1]

class Box(object):
    position = (11,11)
    color = (0, 0, 0)
    num = 0

    def __init__(self, num):
        self.num = num
        self.position = (num*3.25, 11)

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE*2, SIZE*2))
        pygame.draw.rect(surface, self.color, r)


class Cat(object):
    box = 0 
    color = (0, 0, 0)
    position = (0, 0)
    tries = 0
    just_failed = False
    fail_color = (0, 0, 0)

    def __init__(self, box):
        self.box = box
        self.position = (1.5 + (box*3.25), 12.5)
        if not CAT_HIDDEN:
            self.color = (255, 136, 0)

    def move(self):
        self.tries += 1
        self.just_failed = True
        self.fail_color = rand_color()
        if self.box == 1:
            self.box = 2
        elif self.box == BOX_NUMS:
            self.box = BOX_NUMS - 1
        else:
            self.box = self.box + MOVES[rand_move()]
        self.position = (1.5 + (self.box*3.25), 12.5)

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE/2, SIZE/2))
        pygame.draw.rect(surface, self.color, r)

    def win(self):
        self.tries += 1
        print("You found the cat! Total attempts: " + str(self.tries))
        pygame.quit()
        sys.exit(0)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)

    def handle_keypress(self, k):
        if k == pygame.K_1:
            if self.box == 1:
                self.win()
            self.move()
        if k == pygame.K_2:
            if self.box == 2:
                self.win()
            self.move()
        if k == pygame.K_3:
            if self.box == 3:
                self.win()
            self.move()
        if k == pygame.K_4:
            if self.box == 4:
                self.win()
            self.move()
        if k == pygame.K_5:
            if self.box == 5:
               self.win()
            self.move()

def rand_move():
    return random.randint(0, 1)

def rand_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, b, g)


def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    font = pygame.font.Font('freesansbold.ttf', 22)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    cat = Cat(random.randint(1, 5))
    boxes = [Box(i) for i in range(1,6)]

    

    while True:
        cat.check_events()
        draw_grid(surface)

        for box in boxes:
            box.draw(surface) 
        cat.draw(surface)
        
        screen.blit(surface, (0,0))
        for box in boxes:
            screen.blit(font.render(str(box.num), True, (255, 255, 255), None), (box.position[0]*SIZE, box.position[1]*SIZE))
        
        textTries = font.render('Attempts: ' + str(cat.tries), True, (255, 255, 255), None) 
        textRect1 = textTries.get_rect()
        textFail = font.render('Nope, that box is empty! Try again.', True, cat.fail_color, None)
        textRect2 = textFail.get_rect()
        textRect2.center = (WIDTH*SIZE*1/2, HEIGHT*SIZE*.7) 
        screen.blit(textTries, textRect1)
        if cat.just_failed:  
            screen.blit(textFail, textRect2)

        pygame.display.update()

if __name__ == "__main__":
    main()
