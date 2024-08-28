my_string = "LaunchCode"


# # a) Use string methods to remove the first three characters from the string and add them to the end.
# new_string = my_string[3:] + my_string[:3]

# # Use a template literal to print the original and modified string in a descriptive phrase.
# print(f"original string: {my_string}")
# print(f"new string: {new_string}")

# # b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
# num_chars = int(input("Enter number of characters to relocate:"))
# new_string = my_string[num_chars:] + my_string[:num_chars]
# print(f"original string: {my_string}")
# print(f"new string: {new_string}")

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
num_chars = int(input("Enter number of characters to relocate:"))
if num_chars > len(my_string):
    num_chars = 3
    print(f"Error: the number you entereed is longer than the string.")
new_string = my_string[num_chars:] + my_string[:num_chars]
print(f"original string: {my_string}")
print(f"new string: {new_string}")