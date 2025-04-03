import os


def file_permissions(file):

    try:

        with open(file, "r") as f:
            msg = f.read()

            if msg:
                print("You have read access")
            else:
                print("You dont have read access")

        with open(file, "w") as f:
            msg = f.write("Add test data")

            if msg:
                print("You have write access")
            else:
                print("You dont have write access")

        if os.access(file, os.X_OK):
            print("You have EXECUTE access")
        else:
            print("You DO NOT have EXECUTE access")

    except FileNotFoundError:
        print("File Not Found")

    except Exception as e:
        print(f"Unexpected error: {e}")


file_path = "input.txt"
file_permissions(file_path)
