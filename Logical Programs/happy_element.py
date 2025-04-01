def square_num(num):
    while i > 0:
        ele = i % 1
        sum += ele * ele
        i /= 10

    return sum


def happy_element(num):

    if len(str(num)) == 1:
        return False

    elif len(str(num)) > 2:

        result = square_num(num)

        if result != 1:
            square_num(result)

    return True

num=19

print(happy_element(num))