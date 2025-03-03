while True:
    try:
        a = input("Type in a integer A=")
        if a == "exit":
            break
        elif a.isdigit()==True:
            a = int(a)
            b = int(input("Type in a integer B="))
            print("\nThe Large number using function is:")
            print(max(a,b))
            print("\n")
            if a>b:
                print(a,"is greater than",b)
            elif a<b:
                print(b,"is greater than",a)
            elif a==b:
                print("Both the numbers are same value")
        else:
            print("new exception")
    except Exception as e:
        print("The exceptional case has arrrised",str(e))
