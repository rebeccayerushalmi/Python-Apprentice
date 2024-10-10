"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor "red"
tina.pencolor("red")
tina.begin_fill()
tina.fillcolor("red")
tina.forward(160)
tina.left(60)
tina.backward(160)
tina.left(120)
tina.forward(100)
tina.right(60)
tina.forward(160)
tina.end_fill()
tina.penup()
tina.right(120)
tina.forward(30)
tina.pendown()

tina.begin_fill()
tina.fillcolor("yellow")
tina.pencolor("yellow")
for i in range(5):
    tina.right(90)
    tina.backward(100)
    tina.left(90)
    tina.forward(20)
    tina.left(90)
    tina.backward(100)
    tina.right(90)
    tina.forward(20)
tina.right(180)
tina.forward(200)
tina.end_fill()

tina.begin_fill()
tina.fillcolor("#C6A13D")
tina.pencolor("#C6A13D")
tina.forward(20)
tina.right(180)
for i in range(5):
    tina.right(90)
    tina.backward(110)
    tina.left(90)
    tina.forward(20)
    tina.left(90)
    tina.backward(110)
    tina.right(90)
    tina.forward(35)
tina.end_fill()



tina.right(180)
tina.forward(60)

def drawFry():
    tina.setheading(90)
    tina.begin_fill()
    tina.fillcolor("#D3CA63")
    tina.pencolor("#D3CA63")
    tina.forward(50)
    tina.left(90) 
    tina.forward(20)
    tina.left(90)
    tina.forward(50)
    tina.right(90)
    tina.forward(35) 
    tina.end_fill()
drawFry()


turtle.done()
