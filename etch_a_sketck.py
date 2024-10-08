from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_back_forwards():
    tim.backward(10)
def rotate_left():
    tim.left(10)
def rotate_right():
    tim.right(10) 
def clear():
    tim.clear()
    tim.home()               


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back_forwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
