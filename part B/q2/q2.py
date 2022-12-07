# Write a python program to read the contents
# of a file(filename as argument) and store the number of occurrences of each word in a
# dictionary. Display the top 10 words with most number of occurrences in descending order.
# Store the length of each of these words in a list and display the list. Write a one-line reduce
# function to get the average length and one-line list comprehension to display squares of all
# odd numbers and display both.

from functools import reduce


f = open("C:\\Users\\au224\Desktop\\sl lab\\part B\\q2\\text.txt", "r")

x = f.read().split()

itemFrq = dict()
lenList = []
for i in x:
 itemFrq[i] = itemFrq.get(i,0)+1

print(itemFrq)

if len(itemFrq) < 10:
    print("File has less than 10 words")
else:
    print(sorted(itemFrq.items(),key = lambda x : x[1],reverse=True))

for i in itemFrq.keys():
    lenList.append(len(i))

print(lenList)

s = reduce(lambda x,y : x+y,lenList)

print("Average length",s/len(itemFrq))

newList = [x*x  for x in lenList if x%2 == 1]
print(newList)
