import turtle
import math
import time
def draw_heart_outline():
    turtle.speed(0)
    turtle.width(1)
    turtle.hideturtle()
    turtle.bgcolor("black")
    turtle.color("white")
    for t in range(0, 360, 5):
        angle = math.radians(t)
        x = 16 * math.sin(angle) ** 3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        for offset in range(-5, 6, 1):
            turtle.penup()
            turtle.goto(x * 10 + offset, y * 10 + offset)
            turtle.pendown()
            turtle.goto(x * 10 + offset, y * 10 - offset)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.color("white")
    for t in range(0, 360, 5):
        angle = math.radians(t)
        x = 10 * math.sin(angle) ** 3
        y = 8 * math.cos(angle) - 3 * math.cos(2 * angle) - math.cos(3 * angle) - 0.5 * math.cos(4 * angle)
        for offset in range(-2, 3, 1):
            turtle.penup()
            turtle.goto(x * 10 + offset, y * 10 + offset + 150)
            turtle.pendown()
            turtle.goto(x * 10 + offset, y * 10 - offset + 150)
    turtle.penup()
    turtle.goto(-10, 160)
    turtle.pendown()
    turtle.color("white")
    draw_letter_b()
    turtle.hideturtle()
    turtle.done()

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

def draw_first_heart():
    for t in range(0, 360, 5):
        angle = math.radians(t)
        x = 16 * math.sin(angle) ** 3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        for offset in range(-5, 6, 1):
            turtle.penup()
            turtle.goto(x * 10 + offset, y * 10 + offset)
            turtle.pendown()
            turtle.goto(x * 10 + offset, y * 10 - offset)

def draw_second_heart():
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.color("white")
    
    for t in range(0, 360, 5):
        angle = math.radians(t)
        x = 10 * math.sin(angle) ** 3
        y = 8 * math.cos(angle) - 3 * math.cos(2 * angle) - math.cos(3 * angle) - 0.5 * math.cos(4 * angle)
        for offset in range(-2, 3, 1):
            turtle.penup()
            turtle.goto(x * 10 + offset, y * 10 + offset + 150)
            turtle.pendown()
            turtle.goto(x * 10 + offset, y * 10 - offset + 150)

draw_heart_outline()
