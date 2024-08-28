proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for s in strings:
    if ',' in s:
        print(f"'{s}' uses commas as delimiters")
    elif ';' in s:
        print(f"'{s}' uses semicolons as delimiters")
    elif ' ' in s:
        print(f"'{s}' uses spaces as delimiters")

# b) If the string uses commas to separate the words, 
# split it into an array, 
proto_list1 = "3,6,9,12"
list1 = proto_list1.split(',')
print(list1)
# reverse the entries, 
list1.reverse()
print(list1)
# and then join the array into a new comma separated string.
reversed_string = ','.join(list1)
print(reversed_string)


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.



# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.



# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
