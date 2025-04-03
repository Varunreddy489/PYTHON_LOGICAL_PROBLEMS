def replace_word(file, old_word, new_word):

    try:
        with open(file, "r") as f:
            lines = f.readlines()

        with open(file, "w") as f:
            for line in lines:
                f.write(line.replace(old_word, new_word)) 

            print(f"Replaced {old_word} with {new_word} ")

    except FileNotFoundError:
        print("Error File not  found")

    except Exception as e:
        print(e)


file = "input.txt"
old_word = "Hello"
new_word = "Hi"

replace_word(file, old_word, new_word)
