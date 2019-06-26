class ListOpeations():
    list = []

    def append_method(self,x):
        self.list.append(x)

    def display(self):
        print(self.list)

    def delete(self,e):
        if e in self.list:
            self.list.remove(e)
        else:
            print("Element %d is not present in list "%e)

obj = ListOpeations()
while True :
    print("1.Append \n2.Display \n3.Delete \n4.Exit")
    key = input("Choose option : ")
    if key == "1":
        element = int(input("Enter element "))
        obj.append_method(element)
    elif key == "2":
        obj.display()
    elif key == "3":
        element = int(input("Enter element to be deleted :"))
        obj.delete(element)
    elif key == "4":
        break
    else :
        print("Invalid Input")
