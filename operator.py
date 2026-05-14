# num1 = int(input("Enter Fitst Number"))
# num2 = int(input("Enter Second Number"))

# # ============= Arithmetic Operators ===============
# add = num1 + num2
# print(add)

# sub = num1 - num2
# print(sub)

# multi = num1 * num2
# print(multi)

# div = num1 / num2
# print(div)

# floor_res = num1 // num2
# print(floor_res)

# mod = num1 % num2
# print(mod)

# pow = num1 ** num2
# print(pow)

# =================== Assignment Operators =====================

num3 = int(input("Enter Number 3: "))
num4 = int(input("Enter Number 4: "))

num3 += num4
add_assign = num3
print(num3)
print(add_assign)

num3-=num4
print(num3)
add_sub = num3
print(add_sub)

# ========= Bitwise Operator (For Binary Calculations) =======
bit_a = 5 #101
bit_b = 7 #111
bit_c = 10
bit_d = 3

print("BItwise and: ",bit_a & bit_b)
print("BItwise or: ",bit_a | bit_b)
print("BItwise Xor: ",bit_c ^ bit_d)
print("BItwise Left Shift: ",5 << 3)
print("BItwise Right Shift: ",bit_a >> bit_b)