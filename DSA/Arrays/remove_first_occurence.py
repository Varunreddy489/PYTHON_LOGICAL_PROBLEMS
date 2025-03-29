def remove_Ocuurence(arr, ele):
    arr.pop(ele)
    return arr


arr = [1, 2, 3, 4, 5]
ele = 3

result = remove_Ocuurence(arr, ele)

print(f"The result after removing first occurence of {ele} is {result}")
