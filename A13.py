#13.python program to check prime number
n = int(input("enter number : "))
k = 0
for i in range (2,n//2+1):
    if(n%i==0):
        k=k+1
if(k<=0):
    print(n,"is prime number")
else:
    print(n,"is not prime number")
