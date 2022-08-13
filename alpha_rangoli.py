def print_rangoli(size):
    if 0<size<27:
        a='abcdefghijklmnopqrstuvwxyz'
        for i,h,u in zip(range(size,0,-1),range(size-1,0,-1),range(size,0,-1)):
            print('-'*((2*u)-2),end='')
            for j in range(size-1,(i-2),-1):
                if i==size and j==size-1:
                    print(a[j],end='')
                else:
                    print(a[j],end='-')
            for q in range(h+1,size):
                if q==size-1:
                    print(a[q],end='')
                else:
                    print(a[q],end='-')
            print('-'*((2*u)-2))
                

    
        for i,u in zip(range(size),range(1,size+1)):
            print('-'*((2*u)-2),end='')
            for j in range((size-1),0+i,-1):
                print(a[j],end='-')
            for k in range(0+i,size):
                if k==size-1:
                    print(a[k],end='')
                else:
                    print(a[k],end='-')
            print('-'*((2*u)-2))
            

    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)