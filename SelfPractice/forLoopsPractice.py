# numList = [0, 1, 2, 3, 4, 5]
# for num in numList:
#     total = 0
#     total = total + num
# print(total)

# exp = [2340, 2500, 2100, 3100, 2980]
# for i in range(len(exp)):
#     print('Month:', (i+1), 'Expense:', exp[i])
#     total = total + exp[i]

key_location = "chair"
locations = ["garage", "living room", "chair", "closet"]
for i in locations:
    if i == key_location:
        print("key is found in index ", locations.index(i))
        print("or")
        print("key is found in location: " + i)

#Parsing even and odd numbers in a list

listTest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
for i in listTest:
    if i % 2 == 0:
        total = total + 1
        print(i, end = ', ')

print("\nThe total number of even numbers in this list is: ", total)