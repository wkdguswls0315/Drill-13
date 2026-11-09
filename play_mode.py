import game_framework
from pico2d import *
import game_world
from boy import Boy
from grass import Grass

inventory_image = None
inventory_open = False


def handle_events():
    global boy, inventory_open

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode
            game_framework.push_mode(pause_mode)
            return
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_i and
              not getattr(event, 'repeat', 0)):
            inventory_open = not inventory_open
            return
        else:
            boy.handle_event(event)



def init():
    global boy, inventory_image, inventory_open

    game_world.clear()
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)
    inventory_image = load_image('item_select.png')
    inventory_open = False



def update():
    game_world.update()


def pause():
    pass


def resume():
    pass


def render():
    clear_canvas()
    game_world.render()
    if inventory_open:
        inventory_image.draw(400, 300)
    update_canvas()

def finish():
    global boy, inventory_image
    game_world.clear()
    del boy
    del inventory_image
