a=[]
n=int(input("Enter the values you want to read: \n"))
sum=0
for i in range(n):
    element=int(input(f"Enter the values a[{i}]:\n"))
    a. append(element)
for i in range(n):
    for j in range(i+1):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print("sorted array :",a) 
            

    







