# Let's learn a bit about OO programming with classes in Python

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale

rectangle = Shape(100, 50)

# Area of rectangle
print "Rectangle area: "
print rectangle.area()

# Perimeter of rectangle
print "Rectangle perimeter"
print rectangle.perimeter()

# Describe the rectangle
rectangle.describe("A wide rectangle, twice as wide as it is long")

# Set author name
rectangle.authorName("Adrianna Chang")

# Scale it
rectangle.scaleSize(0.5)

print "New rectangle area: "
print rectangle.area() # print new area

# Inheritance in Python
class Square(Shape):
    def __init__(self, x):
        self.x = x
        self.y = x
# The class square inherits from the shape class
