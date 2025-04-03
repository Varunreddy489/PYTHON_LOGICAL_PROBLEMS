def swap_key_values(dict):

    return {x: y for y, x in dict.items()}


dict = {"a": 1, "b": 2}

print(swap_key_values(dict))
