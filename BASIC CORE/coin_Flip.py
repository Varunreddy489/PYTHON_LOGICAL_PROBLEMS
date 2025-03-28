import random


def flip_coin(flip_count):
    """Calculate and print percentage of heads and tails for given number of coin flips

    Arguments : flip_count(int)

    Prints the percentage of heads and tails for given number of coin flips

    """
    heads = 0
    tails = 0

    for _ in range(flip_count):
        result = random.random()
        if result < 0.5:
            tails += 1
        else:
            heads += 1

    head_percentage = (heads / flip_count) * 100
    tail_percentage = (tails / flip_count) * 100

    return (head_percentage, tail_percentage)


flip_count = int(input("How many times should the coin flip: "))

head_percentage, tail_percentage = flip_coin(flip_count)

print(f"Number of flips: {flip_count}")
print(f"Heads Percentage: {head_percentage:.2f}%")
print(f"Tails Percentage: {tail_percentage:.2f}%")
