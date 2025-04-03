def reverse_file_content(input_file, output_file):

    try:
        with open(input_file, "r") as f:
            lines = f.readlines()

        with open(output_file, "w") as f:
            for line in reversed(lines):
                f.write(line)

        print("Reversed the file")

    except FileNotFoundError:
        print("File not  found")

    except Exception as e:
        print(e)


input_file = "input.txt"
output_file = "output.txt"

reverse_file_content(input_file, output_file)
