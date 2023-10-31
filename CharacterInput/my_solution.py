user_name = input("Hello, please input your name :\n")
user_age = input("What is your age:\n")
user_age = int(user_age)
current_year = input("What is the current year?\n")
current_year = int(current_year)
years_to_100 = 100 - user_age
year_to_reach_100 = years_to_100 + current_year
print("Hello", user_name, ". You are", user_age, "in the year", current_year, "and will be 100 in the year", year_to_reach_100)