from pico2d import *
import math

os.chdir('D:/2DGP/DRILL/06 과제 제출/drill-#06 이미지')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

y = 90
x = 400
i = 0


while(1):  
    while(x<780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

        
    while(y<560):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

        
    while(x>20):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)

        
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)


    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)


    while(i<360):
        s = math.sin(i / 360 * 2 * math.pi)
        c = math.cos(i / 360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+(s*210), 300-(c*210))
        i += 2
        delay(0.01)
    i = 0


    
