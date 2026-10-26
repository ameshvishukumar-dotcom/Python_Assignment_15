n=int(input("Enter your number:"))
i=n
fac=1
while i!=0:
    fac*=i
    i-=1
print(f"The factorial of the number {n} is {fac}")
