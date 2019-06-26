sub1 = int(input("Enter mark of the first subject : "))
sub2 = int(input("Enter mark of the second subject : "))
sub3 = int(input("Enter mark of the third subject : "))
sub4 = int(input("Enter mark of the fourth subject : "))
sub5 = int(input("Enter mark of the fifth subject : "))

avg = ( sub1 + sub2 + sub3 + sub4 + sub5 )//5
if(avg >= 90):
    print("Grade : A")
elif ( avg >=80 & avg < 90 ) :
    print("Grade : B")
elif ( avg >=70 & avg < 80 ) :
    print("Grade : C")
elif ( avg >=60 & avg < 70 ) :
    print("Grade : D")
else :
    print("Grade : F")

'''
Enter mark of the first subject : 43
Enter mark of the second subject : 54
Enter mark of the third subject : 65
Enter mark of the fourth subject : 56
Enter mark of the fifth subject : 45
Grade : B
'''
