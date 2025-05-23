def cmult(w,z):
    w1=w[0]
    w2=w[1]
    z1=z[0]
    z2=z[1]
    product=[w1*z1-w2*z2,w1*z2+w2*z1]
    return product
def csetmult(lst):
    n=len(lst)
    i=0
    if n==1:
        return lst
    val=cmult(lst[i],lst[i+1])
    if n==2:
        return val 
    else:
        while i<n-2:
            val=cmult(val,lst[i+2])
            i=i+1
        return val

print(csetmult([(1,1),(5,8),(10,12),(1,10),(1,1)]))