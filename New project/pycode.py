def fac(n):
    if n==0:
        return 1
    else:
        n=n*fac(n-1)

a=fac(5)    
print(a)            