#finding alpha_numeric,alphabetic,digit,lower,upper

if __name__ == '__main__':
    s = input()
    n=s.strip()
    a=[]
    for i in n:
        a.append(i)
    
    
    for j in range(len(a)):
        if a[j].isalnum():
            print(True)
            break
    else:
        print(False)
    
    for j in range(len(a)):
        if a[j].isalpha():
            print(True)
            break
    else:
        print(False)
    
    for j in range(len(a)):
        if a[j].isdigit():
            print(True)
            break
    else:
        print(False)
            
    for j in range(len(a)):
        if a[j].islower():
            print(True)
            break
    else:
        print(False)
        
    for j in range(len(a)):
        if a[j].isupper():
            print(True)
            break
    else:
        print(False)