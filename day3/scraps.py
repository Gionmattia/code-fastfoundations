import math as m

def aa_something():
    a = int(input("Gimme alfa: "))
    b = int(input("Gimme beta: "))
    g = int(input("Gimme gimme more, gimme gimme gimme gamma: "))
    result = a**2 + b**2 - 2 * (a * b) * m.cos(g)
    return result

if __name__ == "__main__":
    c = aa_something()
    print(c)