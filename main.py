from pico2d import *

import game_world
from boy import Boy
from grass import Grass


# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global boy

    grass = Grass()
    game_world.add_object(grass)

    boy = Boy()
    game_world.add_object(boy)


def update_world():
    game_world.update()
    delay(0.001)
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

running = True

open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
