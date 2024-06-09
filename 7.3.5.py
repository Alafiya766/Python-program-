
def remove(str1):
    vowels = "aeiou"
    t = ""
    for char in str1:
        if char in vowels:
            t=t+char
    return t

str1 = input("Enter the input string: ")
print(str1)
str2 = remove(str1)
print("The output string:", str2)
