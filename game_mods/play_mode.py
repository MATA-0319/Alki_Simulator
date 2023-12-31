from pico2d import *

from game_class.class_alki import Alki
from game_class.class_background import Background
from game_class.class_cursor import Cursor
from game_class.class_effect import Effect
from game_class.class_mouse_input import MouseInput
from game_work import game_manager, game_framework
from game_main.config import *


def handle_events():
    global mouse_input, alki

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.stop_run()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.stop_run()
            if event.key == SDLK_SPACE:  # 스페이스바로 게임 시작
                if not mouse_input.input:
                    alki.start = True

        if event.type == SDL_MOUSEMOTION:  # 게임 마우스 입력
            if mouse_input.input and not(alki.pat and mouse_input.click):
                mouse_input.mx, mouse_input.my = event.x, HEIGHT - 1 - event.y

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                if mouse_input.input:
                    mouse_input.click = True

        if event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                if mouse_input.input:
                    mouse_input.click = False


def init():
    global mouse_input, alki

    mouse_input = MouseInput()  # 마우스 입력
    effect = Effect(mouse_input)

    background = Background(effect)  # 배경
    alki = Alki(mouse_input, effect)  # 알키

    game_manager.add_object(mouse_input, 0)
    game_manager.add_object(effect, 0)
    game_manager.add_object(background, 0)
    game_manager.add_object(alki, 1)


def update():
    game_manager.update()


def draw():
    clear_canvas()
    game_manager.render()
    update_canvas()


def finish():
    pass


def pause():
    pass


def resume():
    pass
