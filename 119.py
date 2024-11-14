import turtle as trtl
import time
painter = trtl.Turtle()

#Draw a large triangle.
painter.penup()
painter.goto(-100, 0)
painter.pendown()
for i in range(3):
    painter.forward(500)
    painter.left(120)

#First rectangle
painter.penup()
painter.goto(50, 200)
painter.pendown()
for _ in range(2):
    painter.forward(80)
    painter.left(90)
    painter.forward(40)
    painter.left(90)

#Second rectangle
painter.penup()
painter.goto(180, 200)
painter.pendown()
for _ in range(2):
    painter.forward(80)
    painter.left(90)
    painter.forward(40)
    painter.left(90)

#Connect the rectangles.
painter.penup()
painter.goto(130, 220)
painter.pendown()
painter.forward(50)

#Function to draw an eye
def draw_eye(x, y, color):
    painter.penup()
    painter.goto(x, y)
    painter.pendown()
    painter.fillcolor(color)
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()

#Nose
painter.penup()
painter.goto(130, 150)
painter.pendown()
for _ in range(2):
    painter.forward(50)
    painter.left(120)

#SMILE!
painter.penup()
painter.goto(110, 100)
painter.pendown()
painter.setheading(-60)
painter.circle(50, 120)

#Zigzag beard
painter.penup()
painter.goto(90, 50)
painter.pendown()
painter.setheading(-60)
for i in range(4):
    painter.forward(30)
    painter.left(120)
    painter.forward(30)
    painter.right(120)
    
#Make the eyes change color
colors = ["red", "blue", "green", "yellow", "purple"]
for color in colors:
    draw_eye(80, 210, color)
    draw_eye(210, 210, color)
    time.sleep(0.1)

bgcolor = input("Is it daytime or nighttime? ")
if bgcolor == "nighttime":
    bgcolor = "black"
else:
    bgcolor = "white"

#KEEP
wn = trtl.Screen()
wn.bgcolor(bgcolor)
wn.mainloop()