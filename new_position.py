# def mutate_string(string, position, character):
#     return string[:position]+character+string[position+1:]

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)




# def mutate_string(string, position, character):
    

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)



if __name__ == '__main__':
    s = input()
    a=s.strip()
    l=[]
    for i in a:
        l.append(i)
    
    for j in range(len(l)):
        if l[j].isalnum():
            print(True)
        else:
            print(False)
        if  l[j].isalpha():
            print(True)
        else:
            print(False)
        if l[j].isdigit():
             print(True)
        else:
            print(False)
        if l[j].islower():
            print(True)
        else:
            print(False)
        if l[j].isupper():
            print(True)
        else:
            print(False)



        
        