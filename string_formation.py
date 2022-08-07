def print_formatted(number):
    b=[]
    hex=[]
    z=[]
    alp="ABCDEF"
    Bin=[]
    for bin in range(1,number+1):
       while bin>0:
            c=int(bin%2)
            bin=int(bin/2)           #bin=i
            Bin.append(c)
       Bin.reverse()       #Bin=b
       u=len(Bin)
       # print(u)
       Bin=[]


        

    for i,h,x,g in zip(range(1,number+1),range(1,number+1),range(1,number+1),range(1,number+1)):
        
        while i>0:
            c=int(i%2)
            i=int(i/2)
            b.append(c)
        b.reverse()
        
        k=""           # list into string  /  making string 
        for j in b:
            k+=str(j)
        
        
        while x>0:
            q=int(x%16)
            x=int(x/16)
            d=str(q)
            if q==10:
                d=alp[0]
               
            elif q==11:
                d=alp[1]
               
            elif q==12:
                d= alp[2]
              
            elif q==13:
                d= alp[3]
                
            elif q==14:
                d= alp[4]
                
            elif q==15:
                d= alp[5]
            hex.append(d)
          
        hex.reverse()

        O=""           # list into string  / making string
        for y in hex:
            O+=str(y)

        while g>0:
            s=int(g%8)
            g=int(g/8)
            z.append(s)
        z.reverse()
        
        w=""           # list into string  /  making string 
        for e in z:
            w+=str(e)
        
        print(str(h).rjust(u)+" "+w.rjust(u)+" "+O.rjust(u)+" "+k.rjust(u))
        b=[]
        hex=[]
        z=[]
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)