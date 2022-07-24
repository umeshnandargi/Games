import turtle
import random
wn = turtle.Screen()
wn.title("PONG GAME")
wn.bgcolor('blue')
wn.setup(width = 800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = random.choice((0.1, -0.1))
ball.dy = random.choice((0.1, -0.1))

#Pen
pen= turtle.Turtle()
pen.penup()
pen.color("white")
pen.speed(0)
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=("Courier", 24, "normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    y = y+20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y = y-20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y = y+20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y = y-20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop
while True:
    wn.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=("Courier", 24, "normal"))
    #bounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *=-1