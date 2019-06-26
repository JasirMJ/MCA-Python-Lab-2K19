def numpat(n):
    num = 1
    # outer loop to handle number of rows
    for i in range(0, n):
        # re assigning num
        num = 1
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            print(num, end=" ")
            num = num + 1
        print()

n = 5
numpat(n)