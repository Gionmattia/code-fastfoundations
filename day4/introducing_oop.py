class Circle:
    units = 'cm'  # all circles will have the same units

    def __init__(self, radius, position=(0, 0), fill="white", stroke="black"):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.area = 3.14 * (radius ** 2)
        self.diameter = radius * 2
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


class Rectangle:
    def __init__(self, width, height, fill="white", stroke="black", position=(0, 0)):
        self.width = width
        self.height = height
        self.position = position
        self.fill = fill
        self.stroke = stroke

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def diagonal(self):
        d = (self.width ** 2 + self.height ** 2) ** (1 / 2)
        d = round(d, 3)
        return d

    def bounding_box(self):
        x_min = self.position[0] - self.width / 2
        x_max = self.position[0] + self.width / 2
        y_min = self.position[1] - self.height / 2
        y_max = self.position[1] + self.height / 2
        return x_min, x_max, y_min, y_max

    def __str__(self):
        return (
            f"I am a geometrical shape with perimeter of {self.perimeter()}, diagonal of {self.diagonal()}, and with"
            f" a bounding box values of: {self.bounding_box()}")


donald = Rectangle(4, 6)
print(donald)


class Canvas:
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Text:

    def __init__(self, message, colour, size, position = (0,0)):
        self.message = message # The actual text
        self.position = position # the position
        self.colour = colour # colour of the text
        self.size = size # size of the text


