import json

def update_json(file, key, value):
    try:

        with open(file, "r") as f:
            data = json.load(f)

        data[key] = value

        with open(file, "w") as f1:
            json.dump(data, f1)

        print(f"Updated '{key}' to '{value}' in {file}")

    except FileNotFoundError:
        print("Error not found")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file")

    except Exception as e:
        print(e)


file = "test.json"
key = "email"
value = "varunsannapureddy@gmail.com"

update_json(file, key, value)
