a=input("Enter a number: ")
i = 0
b= 0
while i < len(a):
    if '0' <= a[i] <= '9':
        b += 1
    i += 1  
print("Total digits:", b)
