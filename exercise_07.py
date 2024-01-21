all_nums = []
even_nums = []

while True:
    user_input = input("Enter an integer (or type 'QUIT' to quit): ")

    if user_input == "QUIT":
        break

    number = int(user_input)
    all_nums.append(number)
   
    if number % 2 == 0:
        even_nums.append(number)

print(f"All Nums: {all_nums}")
print(f"Even Nums: {even_nums}")