"""TODO: A picture of a house with a sunset in the background and the moon illuminated... with a star!"""

__author__ = "730411941"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    draw_rectangle(ertle, -318.0, 228.0, 627.0, 70.0, 24, 39, 173)
    draw_rectangle(ertle, -318.0, 158.0, 627.0, 70.0, 27, 47, 224)
    draw_rectangle(ertle, -318.0, 88.0, 627.0, 70.0, 106, 27, 224)
    draw_rectangle(ertle, -318.0, 18.0, 627.0, 70.0, 224, 112, 161)
    draw_rectangle(ertle, -318.0, -52.0, 627.0, 70.0, 226, 156, 112)
    draw_rectangle(ertle, -318.0, -122.0, 627.0, 70.0, 224, 196, 112)
    draw_rectangle(ertle, -318.0, -192.0, 627.0, 70.0, 31, 100, 26)
    draw_rectangle(ertle, -318.0, -298.0, 627.0, 106.0, 50, 159, 43)
    draw_circle(ertle, 200.0, 140.0, 10, 225, 225, 225)
    outline_circle(ertle, 200.0, 140.0, 10, 0, 255, 249)
    draw_circle(ertle, 220.0, 180.0, 2, 198, 198, 198)
    draw_circle(ertle, 238.0, 196.0, 1, 198, 198, 198)
    draw_circle(ertle, 210.0, 168.0, 1, 198, 198, 198)
    draw_circle(ertle, 200.0, 198.0, 0.5, 198, 198, 198)
    draw_square(ertle, -100.0, -192.0, 200.0, 200, 200, 200)
    draw_triangle(ertle, -100.0, 8.0, 200.0, 150, 150, 150)
    draw_square(ertle, -80.0, -62.0, 50.0, 69, 160, 168)
    draw_square(ertle, 30.0, -62.0, 50.0, 69, 160, 168)
    draw_rectangle(ertle, -25.0, -192.0, 50.0, 80.0, 150, 150, 150)
    draw_circle(ertle, 15.0, -162.0, 0.5, 145, 143, 23)
    draw_trapezoid(ertle, -50.0, -298.0, 100.0, 108.91, 200, 184, 145)
    draw_star(ertle, -290.0, 240.0, 20.0, 241, 255, 0)
    done()


def draw_circle(a_turtle: Turtle, x: float, y: float, width: float, r: int, g: int, b: int) -> None:
    """Draw a circle of the given width whose bottom-left index is located at (x, y) with a specific rbg color."""
    colormode(255)
    a_turtle.color(r, g, b)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.speed(50)
    a_turtle.hideturtle()
    a_turtle.begin_fill()
    i: int = 0
    while i < 36:
        a_turtle.forward(width)
        a_turtle.left(10)
        i += 1 
    a_turtle.end_fill()


def outline_circle(a_turtle: Turtle, x: float, y: float, width: float, r: int, g: int, b: int) -> None:
    """Outline a circle of the given width whose bottom-left index is located at (x, y) with a specific rbg color."""
    colormode(255)
    a_turtle.pencolor(r, g, b)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.speed(50)
    a_turtle.hideturtle()
    i: int = 0
    while i < 36:
        a_turtle.forward(width)
        a_turtle.left(10)
        i += 1 


def draw_square(b_turtle: Turtle, x: float, y: float, width: float, r: int, g: int, b: int) -> None:
    """Draw a square of the given width whose bottom-left index is located at (x, y) with a specific rbg color."""
    colormode(255)
    b_turtle.color(r, g, b)
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.pendown()
    b_turtle.speed(50)
    b_turtle.hideturtle()
    b_turtle.begin_fill()
    i: int = 0
    while i < 4:
        b_turtle.forward(width)
        b_turtle.left(90)
        i += 1
    b_turtle.end_fill()


def draw_rectangle(c_turtle: Turtle, x: float, y: float, length: float, height: float, r: int, g: int, b: int) -> None:
    """Draw a rectangle of the given parameters located at (x, y) with a specific rgb color."""
    colormode(255)
    c_turtle.color(r, g, b)
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.pendown()
    c_turtle.speed(50)
    c_turtle.hideturtle()
    c_turtle.begin_fill()
    i: int = 0
    while i < 2:
        c_turtle.forward(length)
        c_turtle.left(90)
        c_turtle.forward(height)
        c_turtle.left(90)
        i += 1
    c_turtle.end_fill()


def draw_triangle(d_turtle: Turtle, x: float, y: float, width: float, r: int, g: int, b: int) -> None:
    """Draw a triangle of the given parameters located at (x, y) with a specific rgb color."""
    colormode(255)
    d_turtle.color(r, g, b)
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.pendown()
    d_turtle.speed(50)
    d_turtle.hideturtle()
    d_turtle.begin_fill()
    i: int = 0
    while i < 3:
        d_turtle.forward(width)
        d_turtle.left(120)
        i += 1
    d_turtle.end_fill()


def draw_trapezoid(e_turtle: Turtle, x: float, y: float, length: float, height: float, r: int, g: int, b: int) -> None:
    """Draw a trapezoid of the given parameters located at (x, y) with a specific rgb color."""
    colormode(255)
    e_turtle.color(r, g, b)
    e_turtle.penup()
    e_turtle.goto(x, y)
    e_turtle.pendown()
    e_turtle.speed(50)
    e_turtle.hideturtle()
    e_turtle.begin_fill()

    e_turtle.forward(length)
    e_turtle.left(103.27)
    e_turtle.forward(height)
    e_turtle.left(76.73)
    e_turtle.forward(50.0)
    e_turtle.left(76.73)
    e_turtle.forward(height)

    e_turtle.end_fill()


def draw_star(f_turtle: Turtle, x: float, y: float, width: float, r: int, g: int, b: int) -> None:
    """Draw a star of the given parameters located at (x, y) with a specific rgb color."""
    colormode(255)
    f_turtle.color(r, g, b)
    f_turtle.penup()
    f_turtle.goto(x, y)
    f_turtle.pendown()
    f_turtle.speed(50)
    f_turtle.hideturtle()
    f_turtle.begin_fill()

    i: int = 0
    while i < 5:
        f_turtle.forward(width)
        f_turtle.left(160)
    
    f_turtle.end_fill()


if __name__ == "__main__":
    main()