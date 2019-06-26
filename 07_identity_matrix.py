n = int(input("Enter a number : "))
for i in range(0,n):
    for j in range(0,n):
        if i == j :
            print("1",sep=" ",end=" ")
        else :
            print("0",sep=" ",end=" ")
    print()

'''
Enter a number : 4
1 0 0 0 
0 1 0 0 
0 0 1 0 
0 0 0 1 
'''
