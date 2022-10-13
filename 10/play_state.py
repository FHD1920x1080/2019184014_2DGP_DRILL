import pico2d
from pico2d import *
import game_framework
import item_state
import random
boy = None
grass = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    list = []

    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = 0
        self.dir = random.randint(0,1)
        if self.dir == 0:
            self.dir = -1
        self.image = load_image('animation_sheet.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = 'BigBall'

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x > 700:
            self.dir = -1
            self.x = 700
        elif self.x < 100:
            self.dir = 1
            self.x = 100



    def draw(self):
        if self.dir ==1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x,self.y + 50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x,self.y + 50)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_i:
                    game_framework.push_state(item_state)

def exit():
    del Boy.list
    del grass

def update():
    for b in Boy.list:
        b.update()

def enter():
    #global boy
    global grass
    boy1 = Boy()
    Boy.list.append(boy1)
    grass = Grass()

def draw_woral():
    grass.draw()
    for b in Boy.list:
        b.draw()

def draw():
    # 게임 월드 렌더링
    clear_canvas()
    draw_woral()
    update_canvas()

def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()


# game main loop code
# finalization code