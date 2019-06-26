class AreaOfRectangle():
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length*self.breadth

length = int(input("Enter length : "))
breadth = int(input("Enter breadth : "))

obj = AreaOfRectangle(length,breadth)
print("Area of rectangle is ",obj.area())
