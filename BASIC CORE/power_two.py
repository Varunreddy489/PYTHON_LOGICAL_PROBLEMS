def powerOf2(num):
    """Calculate and the table of 2 powers till the provided year

    Arguments : num(int)

    Output : 2^1=2
    """

    if num == 0:
        print("1")

    for i in range(num):
        print(f"2^{i+1} is {2**(i+1)}  ")


num = int(input("Enter the Number: "))

powerOf2(num)
