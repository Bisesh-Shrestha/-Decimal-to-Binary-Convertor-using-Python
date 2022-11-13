def or_gate(a,b):
    if a==0 and b==0:
        return 0
    else:
        return 1

def and_gate(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0

def xor_gate(a,b):
    if (a==0 and b==0) or (a==1 and b==1):
        return 0
    else:
        return 1

