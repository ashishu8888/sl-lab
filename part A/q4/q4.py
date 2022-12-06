# Python: Write a temperature converter python program, which is menu driven. Each such
# conversion logic should be defined in separate functions. The program should call the
# respective function based on the user’s requirement. The program should run as long as the
# user wishes so. Provide an option to view the conversions stored as list of tuples with attributes
# - from unit value, to unit value sorted by the user’s choice(from -value or to-value).

past = []

def ctof(c):
    f = round((c*(9/5) + 32))
    a = "from 'c: " + str(c)
    b = "to f: " + str(f)
    store = (a,b)
    past.append(store)
    return f

def ctok(c):
    k = round(273.15 + c)
    a = "from 'c: " + str(c)
    b = "to k: " + str(k)
    store = (a,b)
    past.append(store)
    return k

def ftoc(f):
    c = round((f-32)*(5/9))
    a = "from f: " + str(f)
    b = "to 'c: " + str(c)
    store = (a,b)
    past.append(store)
    return c

def ktoc(k):
    c = round(k - 273.15)
    a = "from k: " + str(k)
    b = "to c: " + str(c)
    store = (a,b)
    past.append(store)
    return c

def ktof(k):
    f = round((k-273.15)*(9/5) + 32)
    a = "from k: " + str(k)
    b = "to f: " + str(f)
    store = (a,b)
    past.append(store)

    return f

def ftok(f):
    k = round((5/9)*(f-32) + 273.15)
    a = "from f: " + str(f)
    b = "to k: " + str(k)
    store = (a,b)
    past.append(store)

    return k

while(1):

 choice = int(input(
    "1.convert c to k\n2.convert k to c\n3.convert c to f\n4.convert f to c\n5.convert k to f\n6.convert f to k\n7.past converstions\n8.Exit\n"))
 
 if choice == 1:
    c = int(input("Enter the temperature in c\n"))
    print("converted temperature to k : \n", ctok(c))
 elif choice == 2:
    k = int(input("Enter the temperature in k\n"))
    print("converted temperature to c : \n", ktoc(k))
 elif choice == 3:
    c = int(input("Enter the temperature in c\n"))
    print("converted temperature to f : \n", ctof(c))
 elif choice == 4:
    f = int(input("Enter the temperature in f\n"))
    print("converted temperature to c : \n", ftoc(f))
 elif choice == 5:
    k = int(input("Enter the temperature in k\n"))
    print("converted temperature to f : \n", ktof(k))
 elif choice == 6:
    k = int(input("Enter the temperature in k\n"))
    print("converted temperature to f : \n", ktof(k))
 elif choice == 7:
    c = int(input("1.Order by from-value\n2.Order by to-value\n"))
    if c == 1:
        print(sorted(past, key=lambda x: x[0]))
    elif c == 2:
        print(sorted(past, key=lambda x: x[1]))
    else:
        print("Invalid input!")
 elif choice == 8:
    break
 else:
    print("Invalid input!")


