def read_large_file(file_path, chunk_size=1024):
    try:
        with open(file_path, "r") as file:
            while chunk := file.read(chunk_size):
                print(chunk, end="")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


file_path = "test.csv"
read_large_file(file_path)
