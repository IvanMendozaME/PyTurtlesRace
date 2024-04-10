from turtle import Turtle, Screen
import random

tim = Turtle()
screen =  Screen()
screen.setup(width=500,height=400)
user_bet =screen.textinput(title="Make your bet", prompt="Which tutle will win the race? ")

colors = ["red", "orange", "black","green", "blue", "purple"]
turtles = []
y = -140
for i in range(6):
    
    tim=Turtle(shape="turtle" )
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y = y)
    turtles.append(tim)
    y+=60

if user_bet:
    is_race_on = True
while is_race_on:
    for i in turtles:
        if i.xcor()>230:
            is_race_on = False
            winning = i.pencolor()
            if i == user_bet:
                print(f"You have won! the {winning} turtle is the winner!")
            else:  
                print(f"You have lost! the {winning} turtle is the winner!")
        i.forward(random.randint(0,10))


screen.exitonclick()