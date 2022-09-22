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

class Circle:
    units = 'cm'  # all circles will have the same units

    def __init__(self, radius, position=(0, 0), fill = "white", stroke = "black"):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.area = 3.14*(radius**2)
        self.diameter = radius*2
        self.fill = fill
        self.stroke = stroke

    def __str__(self):  # Python special methods
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}. Diameter is {self.diameter}, area is {self.area}"

    def peri(self):
        perimeter = 3.14 * 2 * self.radius
        return perimeter

    def arc_length(self, theta, radians=True):
        if radians == True:
            return self.radius * theta
        if radians == False:
            return self.radius * (theta / 180)

    def outbound_box(self):
        x_min = self.position[0] - self.radius
        x_max = self.position[0] + self.radius
        y_min = self.position[1] - self.radius
        y_max = self.position[1] + self.radius
        return x_min, x_max, y_min, y_max

    def draw(self, pen):
        pen.up()
        pen.goto(self.position[0], self.position[1])
        pen.down()
        pen.circle(self.radius)

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

    #def draw_circle(self,circle):
    #    pen = turtle.Turtle()
    #    super().__init__(pen.circle()) # Still no colour

    def draw(self, shape):
        shape.draw(self.pen)



def main():
    #draw_rectangle()
    #draw_circle()
    #draw_triangle()
    #draw_pentagon()
    canvas = Canvas(100,100)
    print(canvas.draw(Circle))
    turtle.done()

    return 0




if __name__ == "__main__":
    sys.exit(main())
