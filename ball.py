from pico2d import load_image

import game_world


class Ball:
    image = None

    def __init__(self, x=400, y=400, velocity=1):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x = x
        self.y = y
        self.velocity = velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        #화면을 벗어나면 객체를 제거해야한다
        if self.x < 0 or self.x > 800:
            game_world.remove_object(self)