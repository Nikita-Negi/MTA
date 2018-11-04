def add(x, y): # This adds two numbers
   return x + y

def sub(x, y):  # This subtracts two numbers
   return x - y

def mul(x, y):  # This multiplies two numbers
   return x * y

def div(x, y): # This divides two numbers
   return x / y

while True:
    print("Welcome to the calculator application:") #Stating the options
    print("--------------------------------------")
    print("Select one operation.")
    print("1.Addition")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("--------------------------------------")

    try:
        choice = input("Enter choice(1/2/3/4):")  # Taking input from the user
        choice = float(choice)

        if choice==1 or choice==2 or choice==3 or choice==4:    #Checking choice of operation to be within range
            num1 = float(input("Enter first number: ")) #Taking numbers as inputs
            num2 = float(input("Enter second number: "))

            if choice == 1:                             #Performing operation based on choice
                print(num1,"+",num2,"=", add(num1,num2))
            elif choice == 2:
                print(num1,"-",num2,"=", sub(num1,num2))
            elif choice == 3:
                print(num1,"*",num2,"=", mul(num1,num2))
            else:
                print(num1,"/",num2,"=", div(num1,num2))

        else:
            print("ERROR:   Invalid choice. Choose again.") #shows error if choice is not within bounds

        print("\nDo you wish to perform another calculation") #Giving the user an option to either exit or continue computing
        again = float(input("Type 1 for Yes and 2 for No:"))
        if again == 1:
            continue
        elif again == 2:
            exit()
        else:
            print("ERROR:   Invalid choice. Choose again.")
    except ValueError:                               #Providing exceptions based on error type
            print("ERROR:   Invalid input. Please provide correct inputs.")

    except ZeroDivisionError:
            print("ERROR:   A number cannot be divided by zero. Please give inputs again.")



