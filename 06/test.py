from pico2d import*
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
while(1):
    x=0
    y=0
    while (x < 360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400+230*math.sin(x/360*2*math.pi), 320+230*math.cos(y/360*2*math.pi))
        x = x + 1
        y = y + 1
        delay(0.01)
    x = 50
    y = 0
    while (x < 750):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 4
        delay(0.01)
    while (y < 450):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(750, 90+y)
        y = y + 4
        delay(0.01)
    while (x > 50):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 540)
        x = x - 4
        delay(0.01)
    while (y > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(50, 90+y)
        y = y - 4
        delay(0.01)

close_canvas()
