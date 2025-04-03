import csv

def column_extractor(file, n):
    try:
        with open(file, "r", newline="", encoding="utf-8") as f1:
            reader = csv.reader(f1)
            column_data = [row[n] for row in reader if len(row) > n]

        return column_data

    except FileNotFoundError:
        print("Error: File not found.")
    except IndexError:
        print(f"Error: Column {n} is out of range.")
    except Exception as e:
        print(f"An error occurred: {e}")


file = "test.csv"
print(column_extractor(file, 1))
