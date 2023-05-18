from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tom = Turtle()
tom.shape("turtle")
tom.color("blue")
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_back():
    tim.back(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def move_forward():
    tom.forward(10)


def move_backward():
    tom.back(10)


def move_left():
    tom.left(10)


def move_right():
    tom.right(10)


def clean():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.onkey(key="i", fun=move_forward)
screen.onkey(key="k", fun=move_backward)
screen.onkey(key="j", fun=move_left)
screen.onkey(key="l", fun=move_right)
screen.onkey(key="space", fun=clean)


screen.exitonclick()
