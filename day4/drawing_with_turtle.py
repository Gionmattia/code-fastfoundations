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
    pen.goto(0, 0)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("white")
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

class Canvas(turtle.TurtleScreen):


    def __init__(self, width, height, bg = "#f12753"):
        canvas = turtle.getcanvas()
        super().__init__(canvas)
        self.screensize(width, height, bg = bg)
        self.pen = turtle.RawTurtle(canvas)
        self.width = width
        self.height = height


    def mystery_method(self):
        self.pen.up()
        self.pen.goto(0, self.height / 2)
        self.pen.down()
        self.pen.goto(0, -self.height / 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.down()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()

    def draw_circle(self,circle):
        pen = turtle.Turtle()
        super().__init__(pen.circle()) # Still no colour

    def draw(self, shape):
        circle.draw(self.shape)
        if pen.isdown():
            pen.up()
        pen.goto(0, 0)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.circle(self.radius)
        pen.end_fill()
        pen.up()

def main():
    #draw_rectangle()
    #draw_circle()
    #draw_triangle()
    #draw_pentagon()
    canvas = Canvas(100,100)
    print(canvas.mystery_method())
    print(canvas.pen.circle(100))
    turtle.done()
    return 0




if __name__ == "__main__":
    sys.exit(main())
