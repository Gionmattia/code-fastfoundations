# OOP day

# I should follow the class examples, but they are boring, so I decided to build a D&D character buildier prototipe using OOP.

class CLASS:
    def __init__(self, level = 1, spellcaster = False):
        self.level = level
        self.spellcaster = spellcaster

    def get_p_bonus(self):
        lvl = self.level
        if lvl < 5:
            return 2
        if 4 < lvl < 9:
            return 3
        if 8 < lvl < 13:
            return 4
        if 12 < lvl < 17:
            return 5
        if lvl > 16:
            return 6

    # Introduce proficiency bonus as subfunction of level

fighter = CLASS()
print(fighter.get_p_bonus())
#print(fighter.level)
#print(fighter.spellcaster)
#print(fighter.proficiency)

class Circle:
    units = 'cm'  # all circles will have the same units

    def __init__(self, radius, position=(0, 0)):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.area = 3.14*(radius**2)
        self.diameter = radius*2

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

# Creating goofy as an element of the circle class
goofy = Circle(15, (1,1))
# Assigning a radius to goofy
print(goofy.area)



print(goofy.outbound_box())
