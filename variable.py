# variables Declaration
name = "Arman"
age = 30
gender = "Male"
grade = 4.88
human = True

print(name)
print(age)
print(gender)

# multiple values on multiple variables
a, b, c = "Amar", "Shonar", "Bangla"
print(a,b,c)

# same vlaue on multiple variable
c = d = e = "Dhaka"
print(d)

# checking Data types
print(type(name), type(age), type(grade), type(human))
check_type = type(d)
print(check_type)

# Type Casting (Explicite)
number = int(grade)
float_age = float(age)
str_number = str(number)

print(number, type(number))
print(float_age, type(float_age))
print(str_number, type(str_number))



# assigment-1
print("Hello World") 
print('Hello World') 
print("You're a good man")
print('''You're a "good" person''')

# Q1: Write a Python program that prints the following text exactly as it appears: 

print("Python is fun.")
print('''"Quotes" and 'single quotes' can be tricky.''')
print("\"Quotes\" and 'single quotes' can be tricky.")

print("Python is fun.\n\"Quotes\" and 'single quotes' can be tricky.")

# Q2: For a business create 3 variables to store- name, age, and city. 
# Then print a sentence that uses these variables.
name2 = "Anik"
age2 = 23 
city = "Madaripur" 
print("My name is", name, "from", city, "& I'm", age )

print(f"My name is {name} from {city} & I'm {age}")

