import turtle

X_START = [0, -20, -40]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for i in range(0,3):
            square = turtle.Turtle(shape="square")
            square.color("white")
            square.penup()
            square.goto(x=X_START[i],y=0)
            self.segments.append(square)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:            
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 

    def add_segment(self, position):          
        square = turtle.Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.segments.append(square)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE)    