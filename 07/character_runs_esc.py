from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True          # Esc를 눌렀을 때, running 값이 False가 되도록 한다.
                        # 이렇게, 달리고 있는 것을 컨트롤 하는 변수를 루프 컨트롤 변수라고 한다.
x = 0
frame = 0


def handle_events():
    # running = False   # 이 running은 위의 running과 다른 변수이다.
    global running      # 함수 밖의 running을 사용하겠다는 선언

    events = get_events()   # get_events()는 list로 넘어오기에 events는 list를 담는 변수가 된다.
    for event in events:    # list에 있는 event 하나씩 꺼내기
        if event.type == SDL_QUIT:      # 마우스로 우측 상단의 x버튼을 눌렀을 경우
            running = False
        #   if event.type == SDL_KEYDOWN:       # SDL_KEYDOWN은 키를 입력받는 것을 말한다.(어떤 종류든)
        #       if event.key == SDLK_ESCAPE:    # SDL에 K를 붙여주면 Key를 의미하는 것 같다. ESCAPE는 ESC를 말한다.
        #           running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  # 위에 처럼 쓸 수 있지만 이렇게 짧게 만들 수 있다.
            running = False


while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 1
    delay(0.01)

close_canvas()

