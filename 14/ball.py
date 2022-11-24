from pico2d import *
import random
import server


class Ball:
    image = None
    font = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        if Ball.font == None:
            Ball.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = random.randint(37, 1800), random.randint(50, 1050)
        self.sx = self.x
        self.sy = self.y

    def update(self):
        pass
    def draw(self):
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        self.font.draw(self.sx - 50, self.sy + 30, '(%d, %d)' % (self.x, self.y), (255, 255, 0))
        self.image.draw(self.sx, self.sy)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.sx - 10, self.sy - 10, self.sx + 10, self.sy + 10