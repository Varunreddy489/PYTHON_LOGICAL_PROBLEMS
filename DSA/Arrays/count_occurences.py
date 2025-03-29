def count_occurence(arr, ele):

    return arr.count(ele)


arr = [1, 2, 3, 4, 5, 2, 3, 3, 2, 2, 6, 7, 8, 9, 10]
ele = 2

result = count_occurence(arr, ele)

print(f"The occurence of {ele} is {result}")
