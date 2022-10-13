from pico2d import *
import game_framework
import title_state
# fill here
image = None
logo_time = 0
def enter():
    global image
    image = load_image('tuk_credit.png')

def exit():
    # fill here
    pass

def update():
    global logo_time
    delay(0.05)
    logo_time += 0.05
    if logo_time > 1:
        game_framework.change_state(title_state)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()