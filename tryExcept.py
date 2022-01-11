#When you run into errors in python, 

#If the user enters anything but an integer, 
# then the 'except' wil trigger and output an error message
try:
    x = int(input('Input an int: '))
    print(x)
except:
    print('Value not an integer. Error!')
