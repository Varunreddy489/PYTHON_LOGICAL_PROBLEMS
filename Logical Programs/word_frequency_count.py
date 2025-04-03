import re


def count(input_file, output_file):
    f = open(input_file, "rt")

    my_str = f.read().lower()

    word_map = {}

    words = re.findall(r"\b\w+\b", my_str)

    for i in words:

        if i not in word_map:
            word_map[i] = 1
        else:
            word_map[i] += 1

    result = open(output_file, "a")
    result.write(str(word_map))
    result.close()


input_file = "input.txt"
output_file = "output.txt"

count(input_file, output_file)
