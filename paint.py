import turtle as turtle_module
import random

turtle_module.colormode(255)
dot = turtle_module.Turtle()
dot.speed("fastest")
dot.penup()
dot.hideturtle()

color_list = [(135, 164, 199), (223, 151, 105), (31, 44, 63), (200, 137, 148), (160, 61, 51), (235, 212, 93), (49, 100, 139), (138, 181, 162), (147, 64, 72), (56, 49, 47), (161, 32, 30), (62, 115, 100), (228, 165, 171), (51, 40, 43), (169, 29, 33), (210, 86, 76), (236, 167, 156), (34, 60, 54), (16, 95, 70), (34, 60, 105), (171, 188, 219), (191, 101, 109), (109, 127, 155), (174, 200, 191), (36, 149, 206), (20, 83, 104)]

screen = turtle_module.Screen()
dot.setheading(230)
dot.forward(300)
dot.setheading(0)
number_of_dots = 100 

for dot_count in range(1, number_of_dots + 1):
    dot.dot(20, random.choice(color_list))
    dot.forward(50)

    if dot_count % 10 == 0:
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        dot.forward(500)
        dot.setheading(0)