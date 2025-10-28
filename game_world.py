world = []

def add_object(obj):
    world.append(obj)

def update():
    for obj in world:
        obj.update()

def render():
    for obj in world:
        obj.draw()