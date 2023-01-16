class Rectangle:
    RectangleCount = 0

    def __init__(self, l, b):
        self.l = l
        self.b = b
        Rectangle.RectangleCount = Rectangle.RectangleCount + 1

    def displayCount():
        print(Rectangle.RectangleCount)

    def area(self):
        return self.l*self.b

l1=int(input("enter l1 "))
b1=int(input("enter b1 "))
l2=int(input("enter l2 "))
b2=int(input("enter b2 "))

r1 = Rectangle(l1,b1)
r2 = Rectangle(l2, b2)

if r1.area() < r2.area():
    print("r2 is greater")
elif r2.area() < r1.area():
    print("r1 is greater")
else:
    print("Both equal")

Rectangle.displayCount()