num = int(input("Enter an integer: "))
float_list = []

for i in range(num):
    float_value = float(input(f"Enter float #{i + 1}: "))
    float_list.append(float_value)

mean = sum(float_list) / num

print(f"List: {float_list}")
print(f"Average: {mean}")
