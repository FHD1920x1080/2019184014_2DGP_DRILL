from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, TIMER, A = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): A
}


class SLEEP:
    @staticmethod
    def enter(self, event):
        print('enter_sleep')
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print('exit_sleep')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        #print('DRAW SLEEP')
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592 / 2, '', self.x + 25, self.y - 30, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, '', self.x - 25, self.y - 30, 100, 100)


# 클래스를 이용하여 상태를 만듦
class IDLE:
    @staticmethod
    def enter(self, event):
        print('enter_idle')
        self.dir = 0
        self.timer = 1000
        pass

    @staticmethod
    def exit(self):
        print('exit_idle')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer <= 0:
            #self.q.insert(0, TIMER)#객체지향 프로그래밍에 위배됨.
            self.add_event(TIMER)
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:  # 오른쪽을 바라보고 있는 상태 #서있음
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:  # face_dir == -1
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
        print('enter_run')
        if event == RD:
            self.dir = 1
        elif event == LD:
            self.dir = -1
        elif event == RU:
            self.dir = -1
        elif event == LU:
            self.dir = 1
        pass

    @staticmethod
    def exit(self):
        print('exit_run')
        # RUN을 나가서 IDLE로 갈때 dir 을 알려주자
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        pass

class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        print('enter_auto_run')
        if self.face_dir == 1:
            self.dir = 1
        else:
            self.dir = -1
        pass

    @staticmethod
    def exit(self):
        print('exit_auto_run')
        # RUN을 나가서 IDLE로 갈때 dir 을 알려주자
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        pass

next_state = {
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, A: AUTO_RUN},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, A: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, A: AUTO_RUN},
    AUTO_RUN: {A: IDLE, RU: AUTO_RUN, LU: AUTO_RUN, RD: RUN, LD: RUN}
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1  # 가는 방향, 바라보는 방향
        self.image = load_image('animation_sheet.png')
        self.timer = 0
        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_events(self, event):
        # 여기에 들어오는 event는 키이벤트이기때문에 내부 RD LU 등으로 변경
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)  # 변환된 이벤트를 큐에 추가

    def update(self):
        self.cur_state.do(self)
        if self.q:  # self.q==True
            event = self.q.pop()  # 이벤트를 가져오고
            self.cur_state.exit(self)  # 현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event]  # 이벤트를 넘겨주고
            self.cur_state.enter(self, event)  # 새로운 이벤트 시작

    def draw(self):
        self.cur_state.draw(self)
