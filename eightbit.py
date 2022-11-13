import reverse as r

#changing binany into 8 bit

def eight_bit(n):
    a= r.rev(n)
    b=[]
    c=[]    
    for i in range (0,8-len(n),1):
        b.append(0)
    b= a+b
    c=r.rev(b)
    return c
