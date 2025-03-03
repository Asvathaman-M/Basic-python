string = input("Type in the String to check for Pallindrome: ")
length = len(string)
if length%2 == 0:
    if string[:(length/2)] == string[-1:-((length/2)+2)]:
        print(string," String is a Pallindrome")
    else:
        print(string," is not a Pallindrome string")
elif length%2 != 0:
    if string[:(length//2)] == string[(length//2)+2:]:
        print(string," String is a Pallindrome")
    else:
        print(string," is not a Pallindrome string")
