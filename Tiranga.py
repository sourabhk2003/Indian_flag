import turtle
import math

def draw_flag(t, length, width, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()

def draw_circle(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_chakra(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(24):
        t.forward(radius)
        t.backward(radius)
        t.right(15)
    t.end_fill()

def draw_tiranga():
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(1)

    # Draw the saffron color part of the flag
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    draw_flag(t, 300, 50, "orange")

    # Draw the white color part of the flag
    t.penup()
    t.goto(-150, 50)
    t.pendown()
    draw_flag(t, 300, 50, "white")

    # Draw the Ashoka Chakra
    t.penup()
    t.goto(0, 25)
    t.pendown()
    draw_chakra(t, 20, "blue")

    # Draw the green color part of the flag
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    draw_flag(t, 300, 50, "green")
    
    
    window.mainloop()

draw_tiranga()
