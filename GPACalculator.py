n = int(input("Please input number of courses: "))

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a/b

def convert(a):
    if a == "A" or a == "a":
        return 5
    elif a == "B" or a =="b":
        return 4
    elif a == "C" or a == "c":
        return 3
    elif a == "D" or a == "d":
        return 2
    else: 
        return 0

credit = []
grade = []

i = 0
while i < n:
    cred_input = int(input("Please input your credit: "))
    credit.append(cred_input)
    grader = input("Please input your grade: ")
    grado = convert(grader)
    gra_cred = multiply(cred_input, grado)
    grade.append(gra_cred)
    i+=1
    continue

credit_sum = sum(credit)
grade_sum = sum(grade)

gpa = divide(grade_sum, credit_sum)


print ("Your total credit is: ", credit_sum)
print ("Your total grade is: ", grade_sum)
print ("Your total GPA is %4.2f" %gpa)
