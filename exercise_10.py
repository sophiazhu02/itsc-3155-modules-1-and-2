user_input = input("Enter a string: ")

characters_list = list(user_input)
nested_lists = []

for i in range(0, len(characters_list), 3):
    sublist = characters_list[i:i+3] 
    nested_lists.append(sublist)

print(nested_lists)

# resource about list() method https://www.programiz.com/python-programming/methods/built-in/list
# resource about sublists http://www.java2s.com/Tutorials/Python/List/How_to_get_sub_list_by_slicing_a_Python_List.htm