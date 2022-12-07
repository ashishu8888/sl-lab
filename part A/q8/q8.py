from functools import reduce

myList = []

print("Enter any 6 numbers")

for i in range(6):
    myList.append(int(input()))

newList = [(lambda x : 3*x) (x) for x in myList]

print(myList)
print(newList)

print(reduce((lambda a,b: a+b),myList))
