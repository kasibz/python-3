import csv
from ValidationException import ValidationException


def validate_file(input_file):
    lines = []
    with open(f"../files/{input_file}", "r") as file:
        lines = file.readlines()

    for line in lines[1:]:
        line_lst = line.split(", ")
        checked_num = line_lst[1]
        try:
            res = int(checked_num)
        except:
            raise ValidationException(f"Invalid mileage:  {checked_num}")


def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)

ex1()