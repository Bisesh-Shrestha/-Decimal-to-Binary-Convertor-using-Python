# reversing a list

def rev(l):
    l2=[]
    for i in range(len(l)-1,-1,-1):
        l2.append(l[i])
    return l2


