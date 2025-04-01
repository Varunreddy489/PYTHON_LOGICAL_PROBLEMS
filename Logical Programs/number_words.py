def number_to_words(n):

    ones = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        10: "ten",
        20: "twenty",
        30: "thirty",
        40: "fourty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    # teens = {
    #     11: "eleven",
    #     12: "twelve",
    #     13: "thirteen",
    #     14: "fourteen",
    #     15: "fifteen",
    #     16: "sixteen",
    #     17: "seventeen",
    #     18: "eighteen",
    #     19: "nineteen",
    # }

    # tens = {
    #     10: "ten",
    #     20: "twenty",
    #     30: "thirty",
    #     40: "fourty",
    #     50: "fifty",
    #     60: "sixty",
    #     70: "seventy",
    #     80: "eighty",
    #     90: "ninety",
    # }

    word = ""

    if n == 0:
        print("Zero")

    if n == 1000:
        print("Thousand")

    if n < 10:
        word = ones[n]

    if n > 10 and n < 20:
        word = ones[n]

    elif n > 100:
        word += ones[n // 100] + "hundred" + " " + "and" + " "
        n = n % 100

        if n in ones:
            word += ones[n]

        elif n in ones:
            word += ones[n]

        else:

            word += ones[n // 10 * 10] + " "

            n = n % 10

            word += ones[n]

    return word


print(number_to_words(653))
