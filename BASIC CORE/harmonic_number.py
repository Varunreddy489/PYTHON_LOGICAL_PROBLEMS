def harmonic_function(n):
    """
    Calculate the sum of harmonic series up to 1/n

    Arguments:
        n (int): The upper limit of denominators in the series (1/1 + 1/2 + ... + 1/n)

    Returns:
        float: Sum of the harmonic series from 1/1 to 1/n

    """

    sum = 0.0

    for i in range(1, n):
        sum += 1 / i

    return sum


upper_limit = int(input("Enter the count of Harmonic value:"))

result = harmonic_function(upper_limit)

print(f"The harmonic sum up to 1/{upper_limit} is: {result:.4f}")
