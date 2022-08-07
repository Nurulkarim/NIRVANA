
def print_formatted(number):
    alp="ABCDEF"
    hex=[]
    for x in range(1,number+1):
        while x>0:
            q=int(x%16)
            x=int(x/16)
            d=str(q)
            if q==10:
                d=alp[0]
                # print(alp[0])
                # print(type(q))
            elif q==11:
                d=alp[1]
                # print(alp[1])
                # print(type(q))
            elif q==12:
                d= alp[2]
                # print(alp[2])
                # print(type(q))
            elif q==13:
                d= alp[3]
                # print(alp[3])
                # print(type(q))
            elif q==14:
                d= alp[4]
                # print(alp[4])
                # print(type(q))
            elif q==15:
                d= alp[5]
                # print(alp[5])
                # print(type(q))
            hex.append(d)
            
        hex.reverse()
        print(hex)
        O=""           # list into string  / making string
        for y in hex:
            O+=str(y)
        
        print(O.rjust(6))

        # b=[]
        hex=[]
       



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
