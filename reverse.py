num=int(input("Enter number"))
r=0
while num!=0:
    d=num%10
    r=r*10+d
    num//=10
print("Reversed number is: "+str(r))