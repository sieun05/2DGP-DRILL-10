# world[0]: 가장 낮은 layer
# world[1]: 그 다음 layer
# ...
world = [[], [], []]

def add_object(obj, depth=0):
    world[depth].append(obj)

def update():
    for layer in world:
        for obj in layer:
            obj.update()

def render():
    for layer in world:
        for obj in layer:
           obj.draw()


def remove_object(obj):
    # 만약 world에 obj가 없는경우... error 처리

    for layer in world:
        if obj in layer:
            layer.remove(obj)
            return      # 성공적으로 제거했으므로 함수 종료

    print("Object not in world")

        
