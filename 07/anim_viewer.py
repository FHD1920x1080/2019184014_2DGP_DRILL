from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
left_character = load_image('left.png')
right_character = load_image('right.png')
frame = 0
x=0
def MyClipDraw(character,left, bottom, width, height, x, y):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(left, bottom, width, height, x, y)
    update_canvas()
    get_events()
    pass

def left_move(p1,p2):
    frame = 0
    for x in range(p1, p2 - 1, -10):
        MyClipDraw(left_character,49*(1+frame), 1340-60, 50, 60, x, 70)
        frame = (frame + 1) % 4  # 0 1 2 3
        delay(0.05)
    pass
def right_move(p1,p2):
    frame = 0
    for x in range(p1, p2 + 1, 10):
        MyClipDraw(right_character, 2600-49*(2+frame), 1340-60, 50, 60, x, 70)
        frame = (frame + 1) % 4
        delay(0.05)
    pass
def left_stop(p,t):
    for t in range(0, t, 1):
        MyClipDraw(left_character, 700, 1340 - 254, 50, 60, p, 70)
        delay(0.5)
        MyClipDraw(left_character, 753, 1340 - 254, 50, 60, p, 70)
        delay(0.5)
    pass
def right_stop(p,t):
    for t in range(0, t, 1):
        MyClipDraw(right_character, 2600-750, 1340 - 254, 50, 60, p, 70)
        delay(0.5)
        MyClipDraw(right_character, 2600-803, 1340 - 254, 50, 60, p, 70)
        delay(0.5)
    pass
def right_pnx(p):
    MyClipDraw(right_character, 2542, 1340 - 650, 56, 60, p, 70)
    delay(0.3)
    for frame in range(0, 4, 1):
        MyClipDraw(right_character, 2492-63*(frame), 1340 - 650, 56, 60, p, 70)
        delay(0.3)
    for frame in range(0, 12, 1):
        MyClipDraw(right_character, 2175-65*(frame), 1340 - 650, 56, 60, p, 70)
        delay(0.2)
    pass
def left_jumpkick(p1,p2):
    r=(p2-p1)//2
    cx=p1+r
    cy=70
    if(r<0):
        r*=-1
    for deg in range(0, 50, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(left_character, 245, 1340 - 60, 50, 60, x, y)
        delay(0.03)
    for deg in range(50, 90, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(left_character, 295, 1340 - 60, 50, 60, x, y)
        delay(0.04)
    for deg in range(90, 120, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(left_character, 345, 1340 - 60, 50, 60, x, y)
        delay(0.04)
    for deg in range(120, 180 + 1, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(left_character, 2470, 1340 - 380, 50, 60, x, y)
        delay(0.03)
    pass
def right_jumpkick(p1,p2):
    r=(p2-p1)//2
    cx=p1+r
    cy=70
    if(r<0):
        r*=-1
    MyClipDraw(right_character, 2135, 1340 - 808, 50, 60, 200, 70)
    delay(0.5)
    for deg in range(180, 160, -5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(right_character, 2078, 1340 - 808, 56, 60, x, y)
        delay(0.02)
    for deg in range(160, 140, -5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(right_character, 2010, 1340 - 808, 56, 60, x, y)
        delay(0.03)
    for deg in range(140, 120, -5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(right_character, 1950, 1340 - 808, 56, 60, x, y)
        delay(0.03)
    for deg in range(120, 100, -5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(right_character, 1890, 1340 - 808, 56, 60, x, y)
        delay(0.04)
    for deg in range(100, 70, -5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(right_character, 1813, 1340 - 808, 71, 60, x, y)
        delay(0.03)
    for deg in range(70, 40, -5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(right_character, 1731, 1340 - 808, 55, 60, x, y)
        delay(0.03)
    for deg in range(40, 20, -5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(right_character, 1657, 1340 - 808, 55, 60, x, y)
        delay(0.03)
    for deg in range(20, 0-1, -5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        MyClipDraw(right_character, 1530, 1340 - 808, 55, 60, x, y)
        delay(0.02)
    pass
while True:
    right_stop(50,1)
    right_move(50,750)
    left_move(750,700)
    left_stop(700,1)
    left_jumpkick(700,300)
    left_move(300,200)
    left_stop(200,1)
    right_stop(200,1)
    right_pnx(200)
    right_jumpkick(200,600)
    right_stop(600,1)
    right_move(600, 750)
    left_stop(750,1)
    left_move(750, 600)
    left_jumpkick(600,200)
    left_move(200, 50)
    left_stop(50,1)

close_canvas()
