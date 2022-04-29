def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter n:"))
r=int(input("Enter r:"))
ncr=fact(n)/(fact(r)*fact(n-r))
print("NcR=",int(ncr))
