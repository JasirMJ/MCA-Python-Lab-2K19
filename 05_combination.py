num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

lst = []

lst.append(num1)
lst.append(num2)
lst.append(num3)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i != j & j != k & k != i):
                print(lst[i],lst[j],lst[k])

'''
Enter first number : 7
Enter second number : 8
Enter third number : 6
7 8 6
7 6 8
8 7 6
8 6 7
6 7 8
6 8 7
'''
