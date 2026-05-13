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