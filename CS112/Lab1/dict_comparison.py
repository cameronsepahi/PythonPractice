from collections import OrderedDict

def main():
    # dict definitions
    cities_zip = dict()
    cities_zip_ordered = OrderedDict()
    # code to read file
    with open('cities.csv') as f:
        # Todo 1: Add code here to iterate over both dictionaries
        for line in f:
            cities_list = line.strip("\n").split(",")
            # Todo 2: Add the cities and their zip codes to both dictionaries
            cities_zip[cities_list[0]] = int(cities_list[1])
            cities_zip_ordered[cities_list[0]] = int(cities_list[1])
        print("(c.)")
        print(cities_zip)
        print("")
        print(cities_zip_ordered)

    def addToDict(dictionary, new_key, new_value):
        #Convert dictionary to list
        newList = list(dictionary.items())
        #Append new_key and new_value (in tuple format) to newList
        newList.append((new_key, new_value))
        #Sort newList such that it's conduscive to instructions 
        newList.sort(key=lambda s: s[0].lower()) #sorting key using lowercase of first item in tuple (city name)
        #Convert list back to dictionary
        newDict = dict(newList)
        print(newDict)
        
    print("(d.)")
    addToDict(cities_zip, "test", 92603)

if __name__ == "__main__":
   main()


