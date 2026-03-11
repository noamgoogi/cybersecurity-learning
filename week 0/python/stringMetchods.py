name = input("Enter your name: ")

len(name) #length of string
name.find(" ") #find the first occurrence of a letter, if there isn't, -1
name.rfind("") #find the last occurrence of a letter, if there isn't, -1
name.capitalize() #Noam barak
name.upper() #NOAM BARAK
name.lower() #noam barak
name.isdigit() #return if a string is only ints, true/false
name.isalpha() #return if a string is only alphabet letters, true/false
name.count("a")
name.replace(" ", "_")

help(str) #every other