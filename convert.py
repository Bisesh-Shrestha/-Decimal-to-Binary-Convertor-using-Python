# Changing from decimal to binary

import reverse as r
def dectobin(n):
    l=[]
    while n!=0:
        if n%2==0:
            l.append(0)
        else:
            l.append(1)
        n= int(n/2)
    l2= r.rev(l)    
    return(l2)


# Changing from binary to decimal

def bintodec(l):
    dec=0
    x=1
    for i in range(len(l)-1,-1,-1):
        dec= dec + x *l[i]
        x = x*2
    return dec

