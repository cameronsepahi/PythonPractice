# def function1():
#     print("test")
#     print("test 2")
# print("this is outside the function")

# def function2(x):
#     return 2*x
# a = function2(3)
# print(a)

def function3(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]
string_list = ['bob', 'alice', 'cameron']

toms_total = function3(tom_exp_list)
joes_total = function3(joe_exp_list)
names_concatenated = function3(string_list)


print("Tom's total expenses: ", toms_total)
print("Joe's total expenses: ", joes_total)
# print("Names concatenation: ", names_concatenated) -> Produces error b/c
# total var (total = 0) is an int, and you're using strings as concatenation data type 

