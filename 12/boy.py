from pico2d import *
from ball import Ball
import game_world

#1 : 이벤트 정의
RIGHT, LEFT, STOP, TIMER, SPACE = range(5)
RD, LD, RU, LU = range(4)
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}
move_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}
# move_able_table = {
#     (RD, LD): RIGHT,
#     (SDL_KEYDOWN, SDLK_LEFT): LD,
#     (SDL_KEYUP, SDLK_RIGHT): RU,
#     (SDL_KEYUP, SDLK_LEFT): LU
# }

#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        if event == SPACE:
            self.fire_ball()

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)


    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir
        if event == SPACE:
            self.fire_ball()

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)


class SLEEP:

    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                          -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)


#3. 상태 변환 구현

next_state = {
    IDLE:  {RIGHT: RUN, LEFT: RUN, STOP:IDLE, TIMER: SLEEP, SPACE: IDLE},
    RUN:   {RIGHT: RUN, LEFT: RUN, STOP:IDLE, SPACE: RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SPACE: SLEEP}
}

class Boy:
    ball_list = []
    def __init__(self):
        self.x, self.y = 800 // 2, 70
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.RIGHT, self.LEFT, self.UP, self.DOWN = False, False, False, False
    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]#여기서 테이블에 없을때 예외처리 해주어야함.
            except KeyError:
                print('Error:',self.cur_state.__name__, event_name[event])
                pass
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir}')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in move_event_table:
            move_event = move_event_table[(event.type, event.key)]
            if move_event == RD:
                self.RIGHT = True
                if self.LEFT == False:
                    self.add_event(RIGHT)
                else:
                    self.add_event(STOP)
            elif move_event == RU:
                self.RIGHT = False
                if self.LEFT == True:
                    self.add_event(LEFT)
                else:
                    self.add_event(STOP)
            elif move_event == LD:
                self.LEFT = True
                if self.RIGHT == False:
                    self.add_event(LEFT)
                else:
                    self.add_event(STOP)
            elif move_event == LU:
                self.LEFT = False
                if self.RIGHT == True:
                    self.add_event(RIGHT)
                else:
                    self.add_event(STOP)
        elif (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fire_ball(self):
        print('FIRE_BALL')
        ball = Ball(self.x, self.y, self.face_dir * 3)
        game_world.add_object(ball, 0)
