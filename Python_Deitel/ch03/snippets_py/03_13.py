# Section 3.13 snippets

# Boolean Operator and
gender = 'Female'
age = 70

if gender == 'Female' and age >= 65:
    print('Senior female')

# Boolean Operator or
semester_average = 83
final_exam = 95

if semester_average >= 90 or final_exam >= 90:
    print('Student gets an A')

# Boolean Operator not
grade = 87

if not grade == -1:
    print('The grade is', grade)

if grade != -1:
    print('The next grade is', grade)
