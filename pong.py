import turtle as trtl
import time

#Get user input for ball color
user_input = input("What is the color of your ball?")

#Create screen
sc = trtl.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width = 1000, height = 600)

#Create left paddle
left_pad = trtl.Turtle()
left_pad.speed(10)
left_pad.shape("square")
left_pad.shapesize(stretch_wid = 6, stretch_len = 2)
left_pad.pu()
left_pad.goto(-400, 0)

#Create right paddle
right_pad = trtl.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.shapesize(stretch_wid = 6, stretch_len = 2)
right_pad.pu()
right_pad.goto(400, 0)

#Create ball
ball = trtl.Turtle()
ball.speed(20)
ball.shape("circle")
ball.color(user_input)
ball.pu()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

#Initialize score
left_player = 0
right_player = 0

#Display the score
score = trtl.Turtle()
score.color = "cyan"
score.pu()
score.hideturtle()
score.goto(0, 260)
score.write("Left player: 0    Right player: 0", align = "center", font = ("Courier", 24, "normal"))

def left_paddleup():
    y = left_pad.ycor()
    if y < 250: #Limit paddle movement
        y += 20
        left_pad.sety(y)

def left_paddledown():
    y = left_pad.ycor()
    if y > -240: #Limit paddle movement
        y -= 20
        left_pad.sety(y)

def right_paddleup():
    y = right_pad.ycor()
    if y < 250: #Limit paddle movement
        y += 20
        right_pad.sety(y)

def right_paddledown():
    y = right_pad.ycor()
    if y > -240: #Limit paddle movement
        y -= 20
        right_pad.sety(y)

#Keyboard bindings
sc.listen()
sc.onkeypress(left_paddleup, "w")
sc.onkeypress(left_paddledown, "s")
sc.onkeypress(right_paddleup, "Up")
sc.onkeypress(right_paddledown, "Down")

#Main game loop
while True:
    sc.update()
    time.sleep(0.01) #Add delay to make the game smoother

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Checking borders
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        score.clear()
        score.write("Left player : {}   Right player: {}".format(left_player, right_player), align = "center", font = ("Courier", 24, "normal"))

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        score.clear()
        score.write("Left player : {}   Right player: {}".format(left_player, right_player), align = "center", font = ("Courier", 24, "normal"))

#Paddle and ball collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < right_pad.ycor() + 50 and ball.ycor() > right_pad.ycor() - 50):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < left_pad.ycor() + 50 and ball.ycor() > left_pad.ycor() -50):
        ball.setx(-360)
        ball.dx *= -1

wn = trtl.Screen()
wn.mainloop()
