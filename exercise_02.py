string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
boolean = string1.endswith(string2) or string2.endswith(string1)
print(boolean)
# used the following resource to learn about the endswith method https://www.tutorialspoint.com/python/string_endswith.htm