name = "Arman"
age = 30
print("Name:", name) #Concatanation 
print(f"Name: {name} \nAge: {age}") #F String


# --------Input------
your_name = input("Your Name: ")
print(your_name)

num1 = int(input("Enter Num1: ")) #Type Casting
num2 = int(input("Enter Num2: ")) #Type Casting

result = num1 + num2

print(result, type(result)) #Input always returns string


# Assignment - 2
# Write a program to input student name & marks of 3 subjects. 
# Print name & percentage in output. 

student_name = input("Enter your name: ")
bangla_marks = input("Enter bangla Marks: ")
maths_marks = input("Enter Maths Marks: ")
science_marks = input("Enter Science Marks: ") 

# calcualating percentage 
percentage = ((int(bangla_marks) + int(maths_marks) + int(science_marks))/300)*100

# # print result 
print(f"The result of {student_name} is {int(percentage)}%. Well done!!")

# optimized solution
print("Percentage Calculator")
student_name2 = input("Enter your name: ")
bangla_marks2 = int(input("Enter bangla Marks: "))
maths_marks2 = int(input("Enter Maths Marks: "))
science_marks2 = int(input("Enter Science Marks: "))

# # calcualating percentage 
percentage = ((bangla_marks2 + maths_marks2 + science_marks2)/300)*100

# # print result 
print(f"The result of {student_name} is {int(percentage)}%. Well done!!")


# Q2: Write a program that collects multiple types of data to store in a dictionary 
# and print output.

#  initializing a dictionary
user_data = {} 

# input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student (yes/no)")

# print the input from user
print(user_data)


