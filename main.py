from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place Your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-30, -60, 0, 30, 60, 90]
all_turtles = []
winner = []


for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winner.append(turtle)
            is_race_on = False
            print(winner[0].pencolor())
            if user_bet in winner[0].pencolor():
                print(f"You've Won! The {user_bet} turtle is the winner.")
            else:
                print(f"You Loose. The {winner[0].pencolor()} turtle is the winner.")

screen.exitonclick()
