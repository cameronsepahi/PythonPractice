#Name: Cameron Sepahi, Lab1 

#---->TASK 1: RANDOM NUMBERS LIST

import random
import time
def randomNumbers(n):
   result = [] 
   while len(result) < n:
      num = random.randint(0,n-1)  
      found = False
      for x in range(len(result)):
         if result[x] == num:
            found = True
            break     
      if not found:
         result.append(num)  
   return result

def randomIndexes(n):
    result = [-1 for x in range(n)]  
    #result = [] -> following 2 lines perform same computation as previous line
        # for x in range(n):
        #     result.append(-1)
    for num in range(n):
        index = random.randint(0,n-1)  
        while result[index] != -1:
            index = random.randint(0,n-1) 
        result[index] = num
    return result

def randomLists(n):
    result = []
    boolCheck = True
    while boolCheck == True:
        randNum = random.randint(0,n-1)  
        result.append(randNum)
        if len(set(result)) == n:
            result = set(result)
            boolCheck = False
    result = list(result)
    random.shuffle(result)
    return result

#---->TASK 2: RANDOM NUMBER LISTS

def randomShuffle(n):
    result = [x for x in range(n)]
    for i in range(n):
        randNum = random.randint(i, n-1)
        result[i], result[randNum] = result[randNum], result[i]
        #if randNum not in result:
         #   result.append(randNum)
    #random.shuffle(result)
    return result

# Displays a comparison in RUNTIME between two functions used to create
#  a random list. Tests sizes 10, 100, 1000, and 10000. May take a long
#  time to finish.
def main():   
   print()  

   # Print the header for the table of runtimes
   print("{:>25s}{:>12s}{:>12s}\n".format("Numbers", "Indexes", "Shuffle"))
   
   # Testing set
   for size in [10,100,1000,10000]:
      
      # Print the lefthand label of the table
      print(" Size: {:>5d} ".format(size), end="", flush=True)
      
      
      # Test each function
      for function in [randomNumbers, randomIndexes, randomShuffle]:
            
         # When did we start the test      
         startTime = time.time()
         
         function(size)
         
         # When did we end the test
         endTime = time.time()
         
         # Display in nice formatting the difference in seconds between starting
         #  and ending the test.
         print("{:>12.4f}".format(endTime - startTime), end="", flush=True)
         
      print() 
   print()
      
# Use this function instead of main() to see the list created by your function.
# Change the line at the bottom of this file to use showList instead of main() to
# Example use: showList(10, randomIndexes)

def showList(n, function):
   print() 
   print(function(n))    
   print()

showList(10, randomShuffle)
   
if __name__ == "__main__":
   main()

