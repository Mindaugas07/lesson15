# 1) Create a function which converts lenght, mass, time units from SI system to CGS. 
# All arguments must hold default values if not provided.

# 2) Create a program which takes 5 random numbers per 1 input.
# The create a function which takes the sum of those numbers (lets agree argument is being called 'num_sum'),
# and all those 5 numbers as separate free arguments as well.
# Multiply all those numbers with with the num_sum you calculated in a list data structure.

# 3) Create lamba functions for these caclulations:
#  - calculate circle Circumference
#  - calculate average speed of the car (knowing distance and time passed to drive that distance)
#  - calculate percentage of value if 5500 is equal 200%

# 1
# def convert_si_to_cgs(seconds: int = 10, meters: int = 10, kilograms: int = 10) -> str:
#     centimeters: int = meters * 100
#     grams: int = kilograms * 1000
#     return f"{seconds} seconds in SI are equal to {seconds} seconds in CGS, {meters} meters in SI equals to {centimeters} centimeters in CGS, {kilograms} kilograms in SI equals to {grams} in CGS."

# print(convert_si_to_cgs())

# 2
from typing import List

num_string: str = input("Please enter 5 random integers like this 1, 2, 5, 76, 89: ")
num_list: List[int] = [int(num) for num in num_string.split(",")]
num_sum = sum(num_list)

def five_random_number_multiplication(num_sum: int, num_list: list) -> List[int]:
    new_list: List[int] = []
    for num in num_list:
        new_list.append(num * num_sum)
    return new_list

print(five_random_number_multiplication(num_sum, num_list))

# 3
# circumference_of_circle = lambda diameter: 3.14 * diameter
# print(circumference_of_circle(4))



