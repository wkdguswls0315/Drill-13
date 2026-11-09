import game_framework
import play_mode
from pico2d import *


def init():
    pass


def finish():
    pass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if (event.type == SDL_KEYDOWN and event.key == SDLK_p and
                not getattr(event, 'repeat', 0)):
            game_framework.pop_mode()
            return


def update():
    pass


def render():
    play_mode.render()
    draw_rectangle(0, 0, 800, 600, 0, 0, 0, 128, True)
    draw_rectangle(370, 260, 390, 340, 255, 255, 255, 255, True)
    draw_rectangle(410, 260, 430, 340, 255, 255, 255, 255, True)
    update_canvas()
