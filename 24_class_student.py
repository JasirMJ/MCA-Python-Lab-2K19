class student:

    def __init__(self,regno,name,place,course):
        self.reg_no = regno
        self.name = name
        self.place = place
        self.course = course

    def show(self):
        print (self.reg_no,"",self.name,"\t",self.course,"\t",self.place)

obj1 = student("\t05","RAM","TVM","MCA")
obj2 = student("\t06","JOHN","MLP","MCA")
obj3 = student("\t08","HARI","EKM","MCA")
obj4 = student("\t09","ALI","PKD","MCA")
obj5 = student("\t02","ROSE","TCR","MCA")

print("Reg No \t Name \t Place \t Course")
obj1.show()
obj2.show()
obj3.show()
obj4.show()
obj5.show()

