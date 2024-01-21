all_nums = []
unique_nums = []

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    all_nums.append(num)

for i in all_nums:
    if all_nums.count(i) == 1:
        unique_nums.append(i)

print(f"Original List: {all_nums}")
print(f"Nums that appear once: {unique_nums}")

# https://www.w3schools.com/python/ref_list_count.asp
# used above link for the count() method