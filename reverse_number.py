# rEVERSE THE NUMBER
number = int(input("Type in the number to be reverse: "))
print("The reverse of the number ",number,end=' is ')
reverse = 0
for i in range(len(str(number))):
    reverse = (reverse * 10) + (number % 10)
    number = number // 10
print(reverse)
    
