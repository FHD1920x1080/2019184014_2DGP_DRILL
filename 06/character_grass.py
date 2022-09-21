from pico2d import*
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
while(1):
    x=0
    y=0
    while (x < 360):#수행시간 360
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400+225*math.sin(x/360*2*math.pi), 315+225*math.cos(y/360*2*math.pi))
        #y최대 540, 최소90 540-90=450, 반지름 225,중앙:225+90
        x = x + 1
        y = y + 1
        delay(0.01)
    x = 50
    y = 0
    while (x < 750):#수행시간 700 4개 총1400+900 2300 원그리기랑 대충 맞추면 6배정도
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 6
        delay(0.01)
    while (y < 450):#수행시간 450
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(750, 90+y)
        y = y + 6
        delay(0.01)
    while (x > 50):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 540)
        x = x - 6
        delay(0.01)
    while (y > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(50, 90+y)
        y = y - 6
        delay(0.01)

close_canvas()