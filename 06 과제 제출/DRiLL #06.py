from pico2d import *
import math

os.chdir('C:/Users/user/Desktop/새 폴더-2d게임 과제')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

y = 90
x = 400
i = 0
s = math.sin(i / 360 * 2 * math.pi)
c = math.cos(i / 360 * 2 * math.pi)


while(1):  
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

        
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

        
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)

        
    while(y>90):
         
        canvas_clear()
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


    while(i<180):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+(s*200), 300+(y*200))
        i += 2
        delay(0.01)



    
