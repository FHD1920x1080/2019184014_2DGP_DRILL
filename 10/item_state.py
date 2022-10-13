from pico2d import *
import game_framework
import play_state

# fill here
image = None
def enter():
    global image
    image = load_image('add_delete_boy.png')
    running = True

def exit():
    # fill here
    pass

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_woral()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    for b in play_state.Boy.list:
                        b.item = 'Ball'
                case pico2d.SDLK_2:
                    for b in play_state.Boy.list:
                        b.item = 'BigBall'
                case pico2d.SDLK_KP_PLUS:
                    boy = play_state.Boy()
                    play_state.Boy.list.append(boy)
                case pico2d.SDLK_EQUALS:
                    boy = play_state.Boy()
                    play_state.Boy.list.append(boy)
                case pico2d.SDLK_KP_MINUS:
                    if len(play_state.Boy.list) > 1:
                        del play_state.Boy.list[len(play_state.Boy.list)-1]
                case pico2d.SDLK_MINUS:
                    if len(play_state.Boy.list) > 1:
                        del play_state.Boy.list[len(play_state.Boy.list)-1]
                case pico2d.SDLK_i:
                    game_framework.pop_state()

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