import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from crossing_scoreboard import Scoreboard

#screen functions
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgpic("E:/AKSHAT/to_be_backed_up/PycharmProjects/GameSpace/images/the_img.gif")
screen.listen()

player = Player()

screen.onkeypress(player.UP, "Up")
screen.onkeypress(player.DOWN,"Down")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()


    #Detect collision with car

    for car in car_manager.the_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
















screen.exitonclick()