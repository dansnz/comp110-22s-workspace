from turtle import Turtle, colormode, done
colormode(255)
circle: Turtle = Turtle()

circle.penup()
circle.goto(0.0, 20.0)
circle.pendown()

i: int = 0

while i < 36:
    circle.left(10)
    circle.forward(20)
    i += 1

i = 0

# hexagon: Turtle = Turtle()

# hexagon.penup()
# hexagon.goto(0.0, 0.0)
# hexagon.pendown()

# i: int = 0
# while i < 6:
#     hexagon.forward(50)
#     hexagon.left(60)
#     i += 1

# i = 0

itzy: Turtle = Turtle()

itzy.penup()
itzy.goto(-318, 0)
itzy.pendown()
while i < 2:
    itzy.forward(627)
    itzy.left(90)
    itzy.forward(298)
    itzy.left(90)
    i += 1

i = 0


done()
