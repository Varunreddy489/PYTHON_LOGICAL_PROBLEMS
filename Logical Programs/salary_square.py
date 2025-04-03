from functools import reduce


def is_age(person):
    return person["age"] >= 25


def salary(my_list):
    return list(filter(is_age, my_list))


def square_salary(person):
    return person["salary"] ** 2


def add(total, salary):
    return total + salary


def main(data):
    return reduce(add, map(square_salary, filter(is_age, data)), 0)


data = [
    {"age": 25, "salary": 30000},
    {"age": 25, "salary": 20000},
    {"age": 21, "salary": 10000},
    {"age": 25, "salary": 60000},
    {"age": 25, "salary": 80000},
]

print(main(data))
