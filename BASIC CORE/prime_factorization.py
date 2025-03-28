def find_prime_factors(number):
    """Compute prime factorization of a number using brute force

    Arguments:
        number (int): The number to factorize

    Returns:
        list: List of prime factors in ascending order
    """
    prime_factors = []
    current_number = number

    if current_number <= 0:
        return prime_factors

    while current_number % 2 == 0:
        prime_factors.append(2)
        current_number = current_number // 2

    i = 3
    while i * i <= current_number:
        while current_number % i == 0:
            prime_factors.append(i)
            current_number = current_number // i
        i += 2

    if current_number > 2:
        prime_factors.append(current_number)

    return prime_factors


input_number = int(input("Enter a number to find its prime factors: "))

if (input_number==0 or input_number==1):
    print("the given number does not have any primes")

factors = find_prime_factors(input_number)

if not factors:
    print("Please enter a positive integer greater than 0")
else:
    print(f"Prime factors of {input_number} are: {factors}")
