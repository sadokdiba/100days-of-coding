from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-330, 330)
        random_y = random.randint(-230,200)
        self.goto(random_x, random_y)

