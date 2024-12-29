from turtle import Screen, Turtle
import time
from Brick import brick
from Ball import Ball
from ScoreBoard import SB
RIGHT_POSITION = (350,0)
LEFTT_POSITION = (-350,0)

screen  = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

t = Turtle()
t.goto(0,300)
t.setheading(270)
t.color("white")
t.width(3)
for i in range (0,60):
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()

r_brick = brick(RIGHT_POSITION)
l_brick = brick(LEFTT_POSITION)
ball = Ball()
sboard = SB()

screen.listen()
screen.onkeypress(r_brick.go_up, "Up")
screen.onkeypress(r_brick.go_down, "Down")
screen.onkeypress(l_brick.go_up, "w")
screen.onkeypress(l_brick.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()
    
    #detecting collision
    #Upper walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    #bricks
    if r_brick.distance(ball) < 50 and ball.xcor() > 320 or l_brick.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_brick()
    #side walls right brick
    if ball.xcor() > 380:
        ball.reset_position()
        sboard.l_point()
    #left brick
    if ball.xcor() < -380:
        ball.reset_position()
        sboard.r_point()
    


screen.exitonclick()