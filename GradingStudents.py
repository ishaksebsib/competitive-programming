# Grading Students

"""
step 1 : create a list of grades
step 2 : create a fucntion that accept list of numbers 
step 3 : create an empty list
step 4 : loop to the list parameter user gives 
step 5 : get round numbuer
step 5 : check the number according to requirements 

"""


# expample step 1 list of grades
grades = [73,67,38,33]


# the function / answer 
def gradingStudents(grades)
    final_grades = []
    for i in grades:
        round = 5 - (i % 5)
        if i < 38:
            final_grades.append(i)
        elif round < 3:
            final_grades.append(i+round)
        else:
            final_grades.append(i)
    return final_grades
  
  
 # example test 
print(gradingStudents(grades))
