from turtle import Turtle
import random
import os


IMAGE_APPLE = os.path.expanduser("./apple.gif")
IMAGE_MOUSE = os.path.expanduser("./rat.gif")
FOODS = [IMAGE_APPLE, IMAGE_MOUSE]


class Food(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.refresh_shape(screen)
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.refresh(screen)

    def refresh(self, screen):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.refresh_shape(screen)
        self.goto(random_x, random_y)

    def refresh_shape(self, screen):
        new_shape = random.choice(FOODS)
        screen.addshape(new_shape)
        self.shape(new_shape)
