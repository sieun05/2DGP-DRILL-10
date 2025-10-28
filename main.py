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

    # 게임월드에 넣는 순서에따라 그려지는 순서가 다르다.

    grass1 = Grass()
    game_world.add_object(grass1, 0)

    grass2 = Grass()
    game_world.add_object(grass2, 2)

    boy = Boy()
    game_world.add_object(boy, 1)


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
