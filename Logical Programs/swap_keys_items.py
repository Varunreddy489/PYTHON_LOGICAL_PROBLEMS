def swap_keys_items(obj1):
    obj2 = {}

    for key, value in obj1.items():
        if value not in obj2:
            obj2[value] = []
        obj2[value].append(key)

    return obj2

input_dict = {"a": 1, "b": 2, "c": 2, "e": 3}
print(swap_keys_items(input_dict))
