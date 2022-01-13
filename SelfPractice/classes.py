#Basic ex:

class Robot:
    #Constructor - need to right self as the first argument in function of constructor
    def __init__(self, name, color, weight): 
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)
        
r1 = Robot("tom", "red", 30)
r2 = Robot("jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def randomNum(self):
        print("The random num is: ", self.x)

p1 = Point(1, 2)
p2 = Point(2, 3)

p1.randomNum()
p2.randomNum()

