#Mat-size M*N(N=M*3)

if __name__=='__main__':
    N,M=map(int,input().split())
    a=int((M-3)/2)
    b=int((M-7)/2)
    
    n=1
    l=N-2
    for i in range(a,1,-3):
        print(('-'*i).ljust(0)+((2*n)-1)*'.|.'+('-'*i).rjust(0))
        n+=1
    for i in range(0,a+1,3):
        if i==0:
            print(('-'*b)+'WELCOME'+('-'*b))
        else:
            print(('-'*i).ljust(0)+l*'.|.'+('-'*i).rjust(0))
            l-=2
    
    