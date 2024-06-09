a=[]
n=int(input("Enter the values you want to read:\n"))
for i in range(n):
    element=int(input(f"Enter the value a[{i}]:"))
    print(element)
    a. append(element)
b=[]
for i in range(n):
    e=int(input(f"Enter the value of b[{i}]:"))
    print(e)
    b. append(element)
for i in range(n):
    if a[i]==b[i]:
        print("Both arrays are equal")
        break
    else:
            print("Not equal")
            break
