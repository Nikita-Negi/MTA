def prime(n): # This checks whether a number is prime or not
    i=0
    count=0
    while i<n :    #only checking divisor property for numbers less than n
        i=i+1
        if n%i==0:  #checking for number of divisors
            count=count+1    #adding to number of divisors if number is divisible
    if count>2:
        return (0)  #returning zero if not prime
    else:
        return (1)  #returning 1 if prime

while True:
    print("\nWelcome to the prime number determination application:") 
    print("--------------------------------------")
    try:
        num = int(input("Enter a number to classify: ")) #Taking number to be checked as input

        ans=prime(num)  #getting the result from prime function 
        if ans==0:
            print("\n",num, "is a not prime number.\n")     #displaying the result
        else:
            print("\n",num, "is a prime number.\n")

        print("\nDo you wish to perform another calculation") #Giving the option to either exit or continue checking        
        again = int(input("Type 1 for Yes and 2 for No:"))
        if again == 1:
            continue
        elif again == 2:
            exit()
        else:
            print("ERROR:   Invalid choice. Choose again.")
    except ValueError:          #defining exceptions that might occur during computations
        print("ERROR:   Invalid input. Try again.")




