username = input("Enter your username: ")

print(len(username) > 12 and username.find(" ") == -1 and username.isdigit() == False)