from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y                 # event.x, event.y는 윈도우 좌표계를 따르기에 pico2d 좌표계로 변환이 필요하다
                                                                     # -1을 넣는 것은 위치가 0부터 시작하기 때문(?) 정확한 보정을 위해 -1을 하는 것
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def move_mouse():
    global x, y, x2, y2, b
    if x2 < x:
        b = 1
        x2 += 1
    elif x2 > x:
        b = 0
        x2 -= 1
    if y2 < y:
        y2 += 1
    elif y2 > y:
        y2 -= 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)

hand_arrow = load_image('hand_arrow.png')
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x2, y2 = x, y
b = 1
frame = 0
hide_cursor()       # 마우스 커서 감추기

while running:
    move_mouse()
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(x, y)
    character.clip_draw(frame * 100, 100 * b, 100, 100, x2, y2)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    delay(0.02)

close_canvas()




