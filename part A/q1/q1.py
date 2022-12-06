
a = []

size = int(input("Enter the size of the list\n"))

for i in range(0,size):
    ele = int(input("Enter the element\n"))
    a.append(ele)

print("The list is",a)

mini = min(a)
maxi = max(a)

print("minimum and maximum elements are: ", mini,maxi)

ele = int(input("Enter the element you want to delete\n"))

a.remove(ele)

print("The modified list is: ", a)

ele = int(input("Enter the element you want to check is there in list\n"))

if ele in a:
    print("Yes,its there\n")

else:
    print("NO,its not there\n")

