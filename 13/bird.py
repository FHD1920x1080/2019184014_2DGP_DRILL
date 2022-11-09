from pico2d import *
import game_framework
import game_world


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 0.3m=30cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0) # 20 * 1000(m) / 분
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)# METER PER MINIT / 초
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity

        self.frame = 0
        self.dir, self.face_dir = 1, 1

        self.timer = 100

        self.font = load_font('ENCR10B.TTF', 16)

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(self.frame * 184, 337, 184, 168, 0, 'h', self.x, self.y, 100, 100)
        elif self.dir == 1:
            self.image.clip_composite_draw(self.frame * 184, 337, 184, 168, 0, '', self.x, self.y, 100, 100)
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))



    def update(self):
        self.frame = (self.frame + 1) % 5

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x >= 1550:
            self.dir = -1
        elif self.x <= 50:
            self.dir = 1
        self.x = clamp(0, self.x, 1600)


    def add_event(self, event):
        self.event_que.insert(0, event)
