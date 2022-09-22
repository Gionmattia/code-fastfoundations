import sys
import turtle


def draw_rectangle():
    turtle.forward(310)
    turtle.right(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(310)
    turtle.right(90)
    turtle.forward(180)


def draw_circle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()

def draw_triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.right(120)

def draw_pentagon():
    for i in range(5):
        turtle.begin_fill()
        turtle.forward(100)
        turtle.right(72)
        turtle.color("blue")
        turtle.end_fill()


def main():
    #draw_rectangle()
    #draw_circle()
    draw_triangle()
    draw_pentagon()
    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
