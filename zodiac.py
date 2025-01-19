
from zodiac_calculator import calculate_zodiac

print("What is your birth month?")
birth_month = int(input())

print("What date of the month were you born?")
birth_date = int(input())

result = calculate_zodiac(birth_month, birth_date)

print(f"You are a  {result})
