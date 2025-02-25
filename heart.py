import turtle
import math
import time

def draw_heart(x_scale, y_scale, offset_range, y_offset=0):
    for t in range(0, 360, 5):
        angle = math.radians(t)
        x = x_scale * math.sin(angle) ** 3
        y = y_scale * (math.cos(angle) - 0.5 * math.cos(2 * angle) - 0.2 * math.cos(3 * angle) - 0.1 * math.cos(4 * angle))
        for offset in offset_range:
            turtle.penup()
            turtle.goto(x * 10 + offset, (y * 10 + offset + y_offset))
            turtle.pendown()
            turtle.goto(x * 10 + offset, (y * 10 - offset + y_offset))

def draw_letter_b():
    turtle.penup()
    turtle.goto(0, 140)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.setheading(0)
    for _ in range(18):
        turtle.forward(2)
        turtle.right(10)
        time.sleep(0.02)
    turtle.setheading(60)
    turtle.forward(10)
    turtle.setheading(0)
    for _ in range(18):
        turtle.forward(2)
        turtle.right(15)
        time.sleep(0.02)
    turtle.penup()
    turtle.goto(0, 160)
    turtle.pendown()

def draw_heart_outline():
    turtle.speed(0)
    turtle.width(1)
    turtle.hideturtle()
    turtle.bgcolor("black")
    turtle.color("white")
    draw_heart(16, 13, range(-5, 6))
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    draw_heart(10, 8, range(-2, 3), y_offset=150)
    turtle.penup()
    turtle.goto(-10, 160)
    turtle.pendown()
    turtle.color("white")
    draw_letter_b()
    turtle.hideturtle()
    turtle.done()

draw_heart_outline()
