a=[4,2,6]
n=int(input("Enter size:"))
print(n)
print("Enter first array:")
print(a)
b=[8,2,6]
print("Enter second array:")
print(b)
if n>0:
    max=a[0]
    min=b[0]
    for i in range(n):
        if a[i] >max:
            max=a[i]
        if b[i]<min:
            min=b[i]
print("Maximum:",max) 
print("Minimum:",min) 
print("Product:",max*min)
