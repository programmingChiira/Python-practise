import datetime

def main():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    current_year = datetime.datetime.now().year
    year_of_100 = current_year + (100 - age)

    print(f"Hi {name}! You will turn 100 years old in the year {year_of_100}.")

if __name__ == '__main__':
    main()
