# Exercise 2

# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        if num % 4 == 0:
            print(f"The number {num} is even and a multiple of 4.")
        else:
            print(f"The number {num} is even but not a multiple of 4.")
    else:
        print(f"The number {num} is odd.")

# Function to check if a number is divisible by another number
def check_divisibility(num, check):
    if num % check == 0:
        print(f"{check} divides evenly into {num}.")
    else:
        print(f"{check} does not divide evenly into {num}.")

# Asking the user for a number
number = int(input("Please enter a number: "))
check_even_odd(number)

# Asking the user for two numbers to check divisibility
num_to_check = int(input("Please enter a number to check: "))
divisor = int(input("Please enter a number to divide by: "))
check_divisibility(num_to_check, divisor)
