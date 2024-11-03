# student_names = ['Sandra',  'Patricia', 'Phiona', 'Anita']
# student_marks = [80, 56, 78, 90]

#  print Patricia, Faith, Phionah and Anitah
# Add Masha at the forth position.
# Update the name Phionah to Phionah Aladina
# Display the length of the student list.
# Print all the students names using a for loop.
# Calculate the total marks for the student marks variable

# SOLUTION


# a)
student_names = ['Sandra',  'Patricia', 'Phionah', 'Anita']
student_marks = [80, 56, 78, 90]

student_names.remove('Sandra')
student_names.insert(1, 'Faith')
print(student_names)

# b)
student_names.insert(4, 'Masha')
print(student_names)

# c)
length = len(student_names)
print(f"The length of this list is {length} names.")

# d)
for student_name in student_names:
    print(student_name)
    
# e)
    sum = 0
    student_marks = [80, 56, 78, 90]
    for mark in student_marks:
        sum+=mark
print(f"The total marks for all student marks is {sum}")


