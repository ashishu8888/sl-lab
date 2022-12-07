
atoms = {"Na" : "sodium" , "Cu" : "copper" , "H": "Hydrogen" , "He" : "Helium"}

print("Dictionary content are: ",atoms)

k = input("Enter the atomic symbol\n")
v = input("Enter the atomic element name\n")

atoms.update({k:v})

print("Dictionary content are: ",atoms)

print(len(atoms))

ele = input("enter a element to search in the dictionary\n")

if ele in atoms.values():
    print("Yes it is")

else:
    print("No, it is not")
