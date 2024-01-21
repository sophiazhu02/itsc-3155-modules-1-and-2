list1 = []
for i in range(5):
    num = int(input(f"Enter a number for the first list: "))
    list1.append(num)

list2 = []
for i in range(5):
    num = int(input(f"Enter a number for the second list: "))
    list2.append(num)

common_list = list(set(list1) & set(list2))

print(f"First List: {list1}")
print(f"Second List: {list2}")
print(f"Common List: {common_list}")

# https://stackoverflow.com/questions/2864842/common-elements-comparison-between-2-lists#comment16339754_2864867
# used the above link to learn about sets