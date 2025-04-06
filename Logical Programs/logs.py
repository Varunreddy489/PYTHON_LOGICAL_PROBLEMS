def extract_errors(log_file, error_file):
    try:
        with open(log_file, "r") as infile, open(error_file, "w") as outfile:
            for line in infile:
                if "ERROR" in line:
                    outfile.write(line)

        print(f"Extracted ERROR messages to {error_file}")

    except FileNotFoundError:
        print("Error: Log file not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


log_file = "logs.txt"
error_file = "error_logs.txt"


extract_errors(log_file, error_file)
