array = []

n = int(input("Enter the number of elements you want to store in the array: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    array.append(element)

print("Elements in the array are:")
for element in array:
    print(element)
