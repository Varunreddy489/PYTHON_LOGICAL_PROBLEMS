def majority_element(nums):

    obj = {}

    for i in nums:
        if i in obj:
            obj[i] += 1

        else:
            obj[i] = 1

    max_value = 0
    max_key = None

    for key, value in obj.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key


nums = [1, 2, 1, 1, 3, 2, 2, 2]
print(majority_element(nums))
