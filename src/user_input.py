
# Interactive user profile program

from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
language = input("Enter your favorite programming language: ")

current_year = datetime.now().year
birth_year = current_year - age
year_turn_100 = birth_year + 100

print("\n--- User Profile ---")
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your favorite programming language is {language}.")
print(f"You will turn 100 around the year {year_turn_100}.")
