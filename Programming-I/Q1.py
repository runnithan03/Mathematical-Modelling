def fermat(a,b,n):
    s=(a**n+b**n)**(1/n)
    return s

print(fermat(3,4,2))