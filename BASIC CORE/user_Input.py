def user_input(name):
    """Taking Name from User"""
    if len(name) < 3:
        print("The User name is less than 3 characters")
    print("Hello " + name + ", How are you?")


userName = input("What is your name: ")
user_input(userName)
