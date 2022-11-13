import convert
import eightbit as e
import bitadder as bad
import reverse as r

#Main module
def main():
    print("\n")
    print("\t\t\t---- Welcome to the Program ----")
    print("\n")
    
    x= int(input("Enter first decimal number: "))    
    if (x>=0 and x<=255):
        y= int(input("Enter second decimal number: "))
        if (y>=0 and y<=255):
            n=convert.dectobin(x)
            m=convert.dectobin(y)
            p=e.eight_bit(n)
            q=e.eight_bit(m)
            a=r.rev(p)
            b=r.rev(q)
            s=0 #sum of a bit
            cin=0 #carry in
            co= 0 #carry out
            rsum=[] #reversed sum    
            for i in range (8):
                s,co= bad.bitadder(a[i],b[i],cin)
                rsum.append(s)
                cin=co
            binary= r.rev(rsum)
            decimal= convert.bintodec(binary)
            print ("The sum in binary is: " + str(binary))  
            print ("The sum in decimal is: " + str(decimal))
            print("\n")
            check= input("If you wish to continue then press 'Yes': ").lower()
            if (check == "yes"):
                main()
            else:
                print("\n")
                print("\t\t\tThank you for using my application!!")
        else:
            print("The input is invalid!!(0-255)")
            main()
    else:
        print("The input is invalid!!(0-255)")
        main()
main()
