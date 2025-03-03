#swap numbers


num1 = int(input("Type in 1st Integer: "))
num2 = int(input("Type in 2nd Integer: "))

copy_num1,copy_num2 = num1,num2     #back holding integer

#case 1
print("\nCase1\nThe case is 'num1,num2 = num2,num1'")
print("\nBefore swap")
print("num1: ",num1,"num2: ",num2)

num1,num2 = num2,num1

print("\nAfter Swap")
print("num1: ",num1,"num2: ",num2,"\n")

# Revert
num1,num2 = copy_num1,copy_num2

#Case2
print("Case2\nThe case is \nnum1 = num1 + num2\nnum2 = abs(num1 - num2)\nnum1 = abs(num1 - num2)")
print("\nBefore swap")
print("num1: ",num1,"num2: ",num2)

num1 = num1 + num2
num2 = abs(num1 - num2)     #abs - absolute function which returns positive value
num1 = abs(num1 - num2)

print("\nAfter Swap")
print("num1: ",num1,"num2: ",num2,"\n")

# Revert
num1,num2 = copy_num1,copy_num2

# Case3
print("Case3\nThe case is \nnum1 = num1 ^ num2\nnum2 = num1 ^ num2\nnum1 = num1 ^ num2")
print("\nBefore swap")
print("num1: ",num1,"num2: ",num2)

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print("\nAfter Swap")
print("num1: ",num1,"num2: ",num2,"\n")
