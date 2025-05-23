#to test if we can write the number in the form (2**n)-1
def ofform(k):
    n=0
    if k==0:
        return True
    else:
        while (2**n)-1<k:
            n=n+1
        if k==(2**n)-1:
            return True
        else:
            return False
        
def isprime(n):
    if n==0 or n==1:
        return False
    if n==2:
        return True
    i=2
    if n>=3:
        while i<=n-1:
            if n%i==0:
                return False 
            else:
                i=i+1
                if i==n:
                    return True
                
def fracmers(lst):
    a=0
    b=0
    i=0
    n=len(lst)
    while i<n:
        if isprime(lst[i]):
            a=a+1
            if ofform(lst[i]):
                b=b+1
            i=i+1
        else:
            i=i+1
    if a==0:
        return("There are no primes")
    else:
        return b/a

print(fracmers([2,3,9]))



            
    
    