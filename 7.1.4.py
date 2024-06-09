a=input("Enter first string:\n")
b=input("Enter second string:\n")
print("Length of first string:",len(a))
print("Length of second string:" ,len(b))
print("Copy of first string:",a) 
print("concatenate:",a+b)
c=a.upper()
print("uppercase of first string:",c) 
if a<b:
    print("First string is alphabetically before second string:")
elif a>b:
    print("First string is alphabetically after second string:")
else:
    print("Bot strings are equal " )

