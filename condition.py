# # ====== if else  =====

# age = int(input("Enter Your Age: "))

# if age >= 18:
#     print("You Can vote!")
# else:
#     print("Sorry You Can't Vote!")
    
# # ========= Check Negative or Positive Number ================
# num1 = int(input("Enter Number: "))

# if num1 < 0:
#     print("Negative")
# elif num1 > 0:
#     print("Positive")
# else:
#     print("Zero")
    
    
# num2 = int(input("Number 2: "))

# if num2 % 2 == 1:
#     print("Odd")
# elif num2 == 0:
#     print("Zero")
# else:
#     print("Even")
    
    

# marks = int(input("Enter Your Marks: "))

# if marks >= 80:
#     print("A+")
# elif marks >= 70:
#     print("A")
# elif marks >= 60:
#     print("A-")
# elif marks >= 50:
#     print("B")
# elif marks >= 40:
#     print("D")
# else:
#     print("F")
    

# -------Nested If ------------
result = input("p or f")
if result == "p":
    marks = int(input("Enter Your Marks: "))

    if marks >= 80:
        print("A+")
    elif marks >= 70:
        print("A")
    elif marks >= 60:
        print("A-")
    elif marks >= 50:
        print("B")
    elif marks >= 40:
        print("D")
    else:
        print("F")
else:
    print("Fail")