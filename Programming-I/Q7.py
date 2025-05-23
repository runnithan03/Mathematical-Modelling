def divisors(n):
    i=1
    lst=[]
    while i<n:
        if n%i==0:
            lst=lst+[i]
        i=i+1
    return lst

def aliquot_successor(n):
    lst=sum(divisors(n))
    return lst

def aliquot_sequence(n):
    lst=[n]
    x=aliquot_successor(n)
    lst.append(x)
    i=0
    while lst[len(lst)-2] != lst[len(lst)-1]:
        x=aliquot_successor(x)
        lst.append(x)
    return lst

def aliquot_pairs(alst):
    lst=[]
    for n in alst:
        i=0
        sequence=aliquot_sequence(n)
        k=len(sequence)
        while i<k:
            pairs=[sequence[i], aliquot_successor(sequence[i])]
            if pairs in lst:
                i=i+1
            else:
                lst.append(pairs)
                i=i+1 
    return lst
        
       

print(aliquot_pairs([6,8,10,18]))
    
    
    
        