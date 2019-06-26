limit = int(input("Enter the number of elements to be inserted : "))
lst = []
for i in range(0,limit):
    element = int(input("enter number : "))
    lst.append(element)
avg = sum(lst)/limit
print("Average of elements in the list ", round(avg,2))


'''
output

============= RESTART: /home/mes/Sumi Python/session1/01_avg.py =============
Enter the number of elements to be inserted : 5
enter number : 1
enter number : 2
enter number : 3
enter number : 4
enter number : 5
Average of elements in the list  3.0
'''
