def compare_files_line_by_line(file1, file2, output_file):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        max_len = max(len(lines1), len(lines2))

        with open(output_file, "w") as o:
            for i in range(max_len):
                line1 = lines1[i].strip() if i < len(lines1) else "Missing in file1"
                line2 = lines2[i].strip() if i < len(lines2) else "Missing in file2"

                if line1 != line2:
                    o.write(f"Line {i+1}:\n")
                    o.write(f"File1: {line1}\n")
                    o.write(f"{line2}\n\n")

        print(f"Differences written to {output_file}")

    except FileNotFoundError:
        print("Error: One or both files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file1 = "input.txt"
file2 = "input2.txt"
output_file = "differences.txt"

compare_files_line_by_line(file1, file2, output_file)
