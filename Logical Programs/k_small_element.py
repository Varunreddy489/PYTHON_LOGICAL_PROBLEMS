def k_small_element(nums,k):
    
    nums.sort()
    print(nums)
    return nums[k-1]

nums=[7, 4, 6, 3, 9, 1]
k = 3

print(k_small_element(nums,k))