# #Finding prime numbers in an interval

# import sys

# start = int(input("Enter your start value: "))
# end = int(input("Enter your end value: "))

# for val in range(start, end + 1):
#     if val > 1:
#         for n in range(2, val//2 + 2):
#             if(val % n) == 0:
#                 break
#             else:
#                 if n == val//2 + 1:
#                     print(val)

# #Python program to print all prime numbers in an interval in a function
# def list_primes(start, end):
#     primes = []

#     for val in range(start, end+1):
#         if val > 1:
#             for n in range(2, val//2+2):
#                 if (val % n) == 0:
#                     break
#                 else:
#                     if n == val//2+1:
#                         primes.append(val)

#     return primes

# print(list_primes(1,5))

# #Types of functions:
#     #Recursive function: function that calls itslef - must have a condition (base case) that determines
#         #when recursion process stops
#     #Nested function: function that is nested in the def of another function
#     #Higher order function: function that receives a function as an argument
#         #and applies it in some way (e.g. map and filter are examples of higher order fns)

# #Python classes

# from random import randint

# class Die(object):
#     "This class represents a six-sided die."

#     def __init__(self):
#         self.value = 1
    
#     def roll(self):
#         self.value = randint(1,6)

#     def getValue(self):
#         return self.value
    
#Example Problems: 
# (1) Given an array of integer nums and an integer target, return
#indices of the two numbers that they add up to the target

output = []

test = [1, 2, 3, 4]
def funcTarget(targetList, target):
    for i in range(len(targetList)):
        if (target - targetList[i+1]) == i:
            output.append(i)
            output.append(i+1)
            break
        
    return output

funcTarget([1,2,3],3)


# (2) Given a string s containing the characters '(',')',{','}','['and']', determine if 
#the input string is valid.

