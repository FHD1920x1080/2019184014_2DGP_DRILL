import math
from pico2d import*

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def rander_all(x,y):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,y)
    update_canvas()
    delay(0.01)
    get_events()
    pass

def Rect():
    print('Rect')
    clear_canvas_now()
    for x in range(50,750+1,10):
        rander_all(x,90)
    for y in range(90,550+1,10):
        rander_all(750,y)
    for x in range(750,50-1,-10):
        rander_all(x,550)
    for y in range(550,90-1,-10):
        rander_all(50,y)
    pass

def Circle():
    print('Circle')
    cx,cy,r=400,300,200
    for deg in range(0,360,1):
        x = cx + r * math.sin(deg/360*2*math.pi)
        y = cy + r * math.cos(deg/360*2*math.pi)
        rander_all(x,y)
    pass

while(True):
    Rect()
    Circle()
    break

close_canvas()