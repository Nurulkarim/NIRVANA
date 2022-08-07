# def print_formatted(number):
#     a=[]
#     for i in range(number+1):
#         while i>0:
#             y=i%2
#             i=i/2
#             a.append(y)
#         print(a)
    
    
        
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

a=int(input())
b=[]
while a>0:
    c=int(a%2)
    a=int(a/2)
    b.append(c)
b.reverse()
print(b)
