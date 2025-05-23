def zeta(s,n):
    x=1
    val=0
    while x<=n:
        a=x**-s
        val=val+a
        x=x+1
    return (val)
print(zeta(2,100))