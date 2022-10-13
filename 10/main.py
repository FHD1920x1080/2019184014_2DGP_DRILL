import pico2d
#import play_state
import logo_state

state = logo_state
#state = play_state
pico2d.open_canvas()
state.enter()

# game main loop code
while state.running:
    state.handle_events()

    #게임 월드 객체를 업데이트
    state.update()

    state.draw()

    state.delay(0.05)

# finalization code
pico2d.close_canvas()
exit()