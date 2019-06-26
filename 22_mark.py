jack = {"name": "Jack Frost",
        "assignment": [89, 50, 40, 20],
        "test": [95, 85],
        "lab": [88.20, 97.20]
        }

james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }

dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 83, 89],
         "test": [88, 87],
         "lab": [80, 80]
         }

def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)

def calculate_total_average(students):
    assignment = get_average(students["assignment"])
    test = get_average(students["test"])
    lab = get_average(students["lab"])

    # Return the result based
    # on weightage supplied
    # 10 % from assignments
    # 70 % from test
    # 20 % from lab-works
    return (0.1 * assignment +
            0.7 * test + 0.2 * lab)

def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"

def class_average_is(student_list):
    result_list = []

    for student in student_list:
        stud_avg = calculate_total_average(student)
        result_list.append(stud_avg)
        return get_average(result_list)

# dictionary of all students
students = [jack,james,dylan]

for i in students:
    print(i["name"])
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Average marks : %s " % ( calculate_total_average(i)))

    print("Letter Grade  : %s" % ( assign_letter_grade(calculate_total_average(i))))

    print()

# Calculate the average of whole class
class_av = class_average_is(students)

print("Class Average is %s" % (class_av))
print("Letter Grade of the class is %s "
      % (assign_letter_grade(class_av)))