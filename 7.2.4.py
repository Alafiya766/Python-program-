strA = input("Enter the first string: \n")
print(strA)
strB = input("Enter the second string: \n")
print(strB)

for char in strB:
    if char not in strA:
        print("Extra character:",char) 
        break

