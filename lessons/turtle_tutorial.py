from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

# leo.forward(50)
# leo.left(30)
# leo.right(40)
# done()

# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# done()

# i: int = 0
# while i < 4:
#     leo.forward(300)
#     leo.left(90)
#     i += 1

# leo.color("magenta")

# leo.pencolor("pink")
# leo.fillcolor(32, 67, 93)
# leo.color("green", "yellow")

leo.color(255, 44, 73)

leo.penup()
leo.goto(-150, -100)
leo.pendown()

leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()

bob.color(89, 56, 255)

bob.penup()
bob.goto(-150, -100)
bob.pendown()

bob.speed(60)
bob.hideturtle()

b: int = 0
while b < 3:
    bob.forward(300)
    bob.left(120)
    b += 1

side_length: float = 300

while b < 150:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(121)
    b += 1

done()