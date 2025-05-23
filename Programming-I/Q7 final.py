def divisors(n):
    i=1
    lst=[]
    while i<n:
        if n%i==0:
            lst=lst+[i]
        i=i+1
    return lst

def aliquot_successor(n):
    return sum(divisors(n))

def aliquot_sequence(n):
    lst=[]
    lst.append(n)
    k=aliquot_successor(n)
    lst.append(k)
    i=0
    val=0
    while lst[i] != lst[i+1]:
        lst.append(aliquot_successor(lst[i+1]))
        i=i+1
    return lst

def ap_for_1_element(n):
    lst=[]
    k=n,aliquot_successor(n)
    lst.append(k)
    i=0
    while lst[i][1] != lst[i][0]:
        lst.append([lst[i][1],aliquot_successor(lst[i][1])])
        i=i+1
    return lst

def aliquot_pairs(alst):
    lst=[]
    n=len(alst)
    i=0
    while i<n:
        k=ap_for_1_element(alst[i])
        lst.append(k)
        i=i+1 
    return lst


print(aliquot_pairs([6,8,10,18]))


        
    
    





    
    

    
        