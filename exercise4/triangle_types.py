"""
Exercise 4
Devise the necessary code in any language to receive 3 values from prompt. Each value
corresponds to the length of the side of a triangle. Values must be Int. A return in a string should
be made stating what type of triangle will these values form.
"""


import traceback
from exercise4.invalid_triangle_exception import InvalidTriangleException


def check_input_validity(sides_input):
    if contains_zero_or_negative_numbers(sides_input) or not is_valid_triangle(sides_input):
        raise InvalidTriangleException("This sequence of numbers doesn't represent a triangle")


def is_valid_triangle(triangle_sides):
    lateral1 = triangle_sides[0]
    lateral2 = triangle_sides[1]
    lateral3 = triangle_sides[2]
    return lateral1 + lateral2 >= lateral3 and lateral2 + lateral3 >= lateral1 and lateral3 + lateral1 >= lateral2


def contains_zero_or_negative_numbers(numbers):
    return sum(1 for number in numbers if number <= 0)


def define_triangle_type(triangle_sides):
    side_one, side_two, side_three = triangle_sides
    if side_one == side_two == side_three:
        return "Equilateral"
    elif side_one == side_two or side_two == side_three or side_three == side_one:
        return "Isosceles"
    else:
        return "Scalene"


def process_input():
    side_one = int(input("Enter the first side of the triangle: "))
    side_two = int(input("Enter the second side of the triangle: "))
    side_three = int(input("Enter the third side of the triangle: "))
    input_list = [side_one, side_two, side_three]
    check_input_validity(input_list)
    return input_list


if __name__ == '__main__':
    try:
        print("This triangle is: " + define_triangle_type(process_input()))
    except InvalidTriangleException as error:
        print(error)
    except ValueError as input_error:
        print("Invalid input: " + str(input_error))
    except Exception:
        traceback.print_exc()
