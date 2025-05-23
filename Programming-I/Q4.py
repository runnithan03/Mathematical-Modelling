def cmult(w,z):
    w1=w[0]
    w2=w[1]
    z1=z[0]
    z2=z[1]
    product=[w1*z1-w2*z2,w1*z2+w2*z1]
    return product

print(cmult([1.0,2.0],[3.0,4.0]))