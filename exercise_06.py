row_num = int(input("Enter a row num from 1 to 5: "))
column_num = int(input("Enter a col num from 1 to 5: "))

for i in range(1, 6):
        for j in range(1, 6):
            if i == row_num and j == column_num:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()