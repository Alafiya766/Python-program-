string = input("Enter a string: \n")
unique=""
for char in string:
    if char not in unique:
        unique=unique+char
print("removed string:",unique) 

