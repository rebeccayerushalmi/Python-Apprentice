"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location


    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

"""
import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.penup()
t.shape("turtle")
def screen_clicked(x, y):


    print('You pressed: x=' + str(x) + ', y=' + str(y))

    t.goto(x, y)
screen.onclick(screen_clicked)
turtle.done()

