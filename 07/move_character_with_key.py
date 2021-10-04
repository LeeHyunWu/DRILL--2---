from pico2d import *


def handle_events():
    global running      # running이 정의된 함수는 아래에 있지만 함수 선언은 ~~한 것이 있다라고만 하는 것 뿐이므로 괜찮다.
    global dir            # 함수에서 정의된 global 변수는 함수가 직접 실행되기 전까지 선언되어있으면 된다.
    global b
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                b = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                b = 0
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1



open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
b = 1
frame = 0
dir = 0             # 방향을 나타내는 변수, -1은 왼쪽방향, +1은 오른쪽 방향으로 움직이게 한다.

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * b, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5

    delay(0.1)

close_canvas()

