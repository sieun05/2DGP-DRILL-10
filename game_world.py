world = []

def add_object(obj):
    world.append(obj)

def update():
    for obj in world:
        obj.update()

def render():
    for obj in world:
        obj.draw()


def remove_object(obj):
    if obj in world:
        world.remove(obj)
    else:
        print("Object not in world")
        
    # 만약 world에 obj가 없는경우... error 처리