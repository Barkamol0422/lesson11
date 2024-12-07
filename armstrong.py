a=int(input())
b=0
c=a
while c>0:
    d=c%10
    b+=d**3
    c=c//10
if a==b:
    print(a,'is Armstrong number')
else:
    print(a,'is not armstrong number')
    
