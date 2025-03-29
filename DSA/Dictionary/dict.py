# * sort (ascending and descending) a dictionary by value


def sort_Dictionary(d):
    return {key: d[key] for key in sorted(d)}


d = {"a": 1, "c": 3, "b": 2}

print(sort_Dictionary(d))

# * add a element to a dictionary.


def add_ele(dict, key, value):
    dict[key] = value

    return dict


print(add_ele({0: 10, 1: 20}, 2, 30))

# *  add a key to a dictionary.


def add_dict(dict1, dict2):
    dict1.update(dict2)
    return dict1


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

print(add_dict(dict1, dict2))

# *   iterating over dictionaries using for loop.


def iterate_dict(dict):

    for x, y in dict.items():
        print(x, y)


dict = {"a": 1, "b": 2, "c": 3}


# *  generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).


def square_dict(n):

    return {x: x * x for x in range(1, n + 1)}


print(square_dict(5))

# * remove a key from a dictionary


def remove_key(dict, key):
    dict.pop(key)
    return dict


dict = {"a": 1, "b": 2, "c": 3}
key = "b"

print(remove_key(dict, key))


# *  print all unique values in a dictionary.


def print_unique(dict):
    list = []

    for x in dict.values():
        if x not in list:
            list.append(x)
    return list


dict = {"a": 1, "b": 2, "c": 3, "d": 3}

print(print_unique(dict))


# * create a dictionary from a string.


def create_dict(str):
    dict = {}

    for i in str:
        dict[i] = dict.get(i, 0) + 1

    return dict


print(create_dict("Hello World"))


# *  print a dictionary in table format


def print_dict_table(dict):

    print("{:<10} {:<10} ".format("KEY", "VALUE"))

    for key, value in dict.items():
        print("{:<10} {:<10}".format(key, value))


dict = {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50,
}

print_dict_table(dict)

# * count the values associated with key in a dictionary.
# * Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
# * False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]


def associated_keys(list):
    count = 0

    for i in list:
        if i["success"]:
            count += 1

    return count


list = [
    {"id": 1, "success": True, "name": "Lary"},
    {"id": 2, "success": False, "name": "Rabi"},
    {"id": 3, "success": True, "name": "Alex"},
]

print(associated_keys(list))

# Todo convert a list into a nested dictionary of keys.


# * Write a Python program to check multiple keys exists in a dictionary


def count_keys(dict):
    count = 0

    for i in dict.keys():
        count += 1

    return count


dict = {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
}

print(count_keys(dict))

# * Write a Python program to count number of items in a dictionary value that is a list.


def is_value_list(dict):
    count = 0
    for i in dict.values():
        if type(i) == list:
            count += 1
    return count


dict = {1: [1, 2, 3], 2: 20, 3: [10, 20, 30]}

print(is_value_list(dict))
