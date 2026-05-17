# name = "Arman"
# age = 30
# print("Name:", name) #Concatanation 
# print(f"Name: {name} \nAge: {age}") #F String


# # --------Input------
# your_name = input("Your Name: ")
# print(your_name)

# num1 = int(input("Enter Num1: ")) #Type Casting
# num2 = int(input("Enter Num2: ")) #Type Casting

# result = num1 + num2

# print(result, type(result)) #Input always returns string


# # multple input from user 
# # input from user to add two number and print result
# x = input("Enter first number: ")
# y = input("Enter second number: ") 
# print(f"Sum of {x} & {y} is {int(x) + int(y)}")

# HW: write a program to input student name and marks of 3 subjects. 
# And print name and percentage in output.   

student_name = input("Enter Your Name: ")

bangla = int(input("Bangla Marks: "))
english = int(input("English Marks: "))
math = int(input("Math Marks: "))

average = (bangla + english + math) / 3

print(f"{student_name} got {average}%")
