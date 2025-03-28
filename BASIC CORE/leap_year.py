def is_leap_year(year):
    """Determine if the provided year is a leap year

    Arguments:
        year (int): The year to check

    Returns:
        bool: True if leap year, False otherwise

    Leap Year Rules:
        - Divisible by 4
        - If divisible by 100, must also be divisible by 400
    """
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    return False


input_year = int(input("Enter the Year: "))
result = is_leap_year(input_year)

print(result)

if result:
    print(f"The Year {input_year} is a Leap Year")
else:
    print(f"The Year {input_year} is not a Leap Year")
