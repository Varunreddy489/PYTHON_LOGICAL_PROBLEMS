def perfect_square(num):

    low = 1
    high = num - 1

    while low <= high:

        mid = (low + high) // 2

        if mid * mid == num:
            return True

        elif mid * mid > num:

            high = mid - 1

        else:
            low = mid + 1

    return False


print(perfect_square(20))
print(perfect_square(25))
