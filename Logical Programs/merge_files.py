def merge_files(file1, file2):

    try:

        with open(file1, "r") as f1:
            file1_lines = f1.readlines()

        with open(file2, "r") as f2:
            file2_lines = f2.readlines()

        if file1_lines == file2_lines:

            with open(output_file, "w") as out:
                out.writelines(file1_lines)
                out.writelines(file2_lines)

        else:

            if file1_lines > file2_lines:

                with open(output_file, "w") as out:
                    out.writelines(file2_lines)

            else:
                with open(output_file, "w") as out:
                    out.writelines(file2_lines)

        print(f"Merged {file1} and {file2} into {output_file}")

    except FileNotFoundError:
        print("Error not found")

    except Exception as e:
        print(e)


input_file = "input.txt"
output_file = "input2.txt"

merge_files(input_file, output_file)
