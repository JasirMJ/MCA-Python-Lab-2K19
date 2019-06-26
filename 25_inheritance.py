class Vehicle(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def wheel(self):
        return "4 wheels"

class Bike(Vehicle):

    def wheel(self):
        return "2 wheels"

# Driver code
obj = Vehicle("Car")  # An Object of Person
print(obj.getName()," has ", obj.wheel())

obj = Bike("Pulsar")  # An Object of Employee
print(obj.getName()," has ",  obj.wheel())


# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#
#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
#
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])
#
# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)
#
#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)
#
# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()