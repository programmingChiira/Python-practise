# Exercise 3

# Given list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Printing elements less than 5
print("Elements less than 5:")
for element in a:
    if element < 5:
        print(element, end=" ")

# Creating a new list with elements less than 5
new_list = [element for element in a if element < 5]
print("\nNew list with elements less than 5:", new_list)

# Using a one-liner to print elements less than 5
print("One-liner elements less than 5:", [element for element in a if element < 5])

# Asking the user for a number and returning elements less than the user's input
user_input = int(input("Please enter a number: "))
filtered_list = [element for element in a if element < user_input]
print(f"List with elements less than {user_input}:", filtered_list)
