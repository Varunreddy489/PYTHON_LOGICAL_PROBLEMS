def sum_of_2_nums(nums, target):
    num_map = {}  

    for i in range(len(nums)):  
        num = nums[i]
        complement = target - num  

        if complement in num_map:  
            return [num_map[complement], i]  

        num_map[num] = i  

    return []  


nums = [2, 7, 11, 15]
target = 9
print(sum_of_2_nums(nums, target))  
