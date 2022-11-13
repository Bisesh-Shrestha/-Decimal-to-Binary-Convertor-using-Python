import gates as g

def bitadder(a,b,cin):
    #for sum
    s1= g.xor_gate(a,b) 
    fs= g.xor_gate(s1,cin) #fs = final sum

    #for carry over
    co1= g.and_gate(a,b)
    co2= g.and_gate(s1,cin)
    co= g.or_gate(co1,co2) #co= carry out

    return fs, co

