# Function to find divisors of a number
def find_divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

# Asking the user for a number
number = int(input("Please enter a number: "))

# Printing the list of divisors
divisors_list = find_divisors(number)
print(f"The divisors of {number} are: {divisors_list}")