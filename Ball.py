from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def movement(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)
    
    def bounce_wall(self):
        self.y_move *= -1
    
    def bounce_brick(self):
        self.x_move *= -1
        self.move_speed *= 0.7
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_brick()