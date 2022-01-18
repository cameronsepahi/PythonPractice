
def productSum(numbers1, numbers2):
    output = 0
    for i in range(len(numbers1)): 
        output += numbers1[i] * numbers2[i]
    return output

def minSum(list1, list2):
    connect = []
    for i in range(len(list1)):
        connect.append((list2[i], list1[i]))
    connect.sort()
    new_list1 = []
    for i in connect:
        new_list1.append(i[1])
    return productSum(new_list1, list2)

test1 = [5,3,4,2]
test2 = [4,2,2,5] 
numbers1 = [ 2, 4, 5, 8, 3, 1 ]
numbers2 = [ 10, 4, 8, 9, 5, 7 ]
print(minSum(numbers1, numbers2))
