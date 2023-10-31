number = int(input("Enter any number :\n"))
if number % 2 == 0:
    print("The number is an even number")
elif number % 2 != 0:
    print("The number is an odd number")
else:
    print("Please input a number")
    number = int(input("Enter any number :\n"))