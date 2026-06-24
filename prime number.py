number=int(input("enter a number:"))
if number==0 or number==1:
    print("The number is neither prime nor composite.")
elif number<0:
    print("Invalid input. Please enter a positive integer.")
elif number>1:
    if number==2:
        print("The number is a prime.")
    elif number%2==0:
        print("The number is not a prime.")
    else:
        s=number+1
        for i in range(2, s//2):
            if number%i==0:
                print("The number is not a prime.")
                break
        else:
            print("The number is a prime.")
