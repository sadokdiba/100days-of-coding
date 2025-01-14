from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        if random.randint(0, 5) == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            new_car.penup()
            random_y = random.randint(-220, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
            
