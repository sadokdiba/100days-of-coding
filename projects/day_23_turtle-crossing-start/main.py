import time
from turtle import Screen
from player import Player
import car_manager as c
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = c.CarManager()
scoreb = Scoreboard()
    
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreb.game_over()
            
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreb.increase_level()

screen.exitonclick()