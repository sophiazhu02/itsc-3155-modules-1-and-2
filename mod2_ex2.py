string = input("Enter a string: ")

lowercase_letters = ''.join(c for c in string if c.islower())
uppercase_letters = ''.join(c for c in string if c.isupper())
    
    # Remove spaces
user_input_no_spaces = ''.join(c for c in string if c != ' ')

    # Construct the result
result = lowercase_letters + uppercase_letters

print(result)