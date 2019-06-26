a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b = set()
duplicate = []
for x in a:
    if x not in b:
        b.add(x)
    else :
        duplicate.append(x)
print("duplicate items:")
print(duplicate)