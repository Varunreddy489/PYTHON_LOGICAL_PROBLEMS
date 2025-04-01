def reverse_array(nums):

    half = len(nums) // 2
    size = len(nums)

    for i in range(half):

        nums[i], nums[size - i - 1] = nums[size - i - 1], nums[i]

    return nums

nums=[1, 2, 3, 4, 5]

print(reverse_array(nums))