
#beautiful code
#making list into string and string into integer.
# if __name__ == '__main__':
#     n = int(input())
#     if 1<=n<=150:
#         a= [i for i in range(1,n+1)] 
#         string=""                    
#         for j in a:
#             string+=str(j)
#             b=int(string)
#         print(b)
        
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     a=[[i,j,k]for i in range(x+1)for j in range(y+1)for k in range(z+1)if i+j+k!=n]
#     print(a)


#success after trying | runner up solution | hacker rank
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     a=list(arr)
#     a.sort()
#     b=max(a)
#     c=a.index(b)
#     d=c-1
#     print(a[d])



# if __name__ == '__main__':
#     a=[]
#     num=[]
#     tum=[]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         a.append([name,score])
#         tum.append(name)
#         num.append(score)
#         num.sort(reverse=True)
#         b=min(num)
#         while num.count(b)>1:
#             num.pop()
#         num.sort()
#     t=1
#     e=num[t]
#     f=num[t+1]
#     if num.count(num[t])>1:
#         print(tum[t])
#         print(tum[t+1])
        
#     else:
#         print(tum[t])


#     # while True:
#     #     if e==f:
#     #         print(tum[t])
#     #         print(tum[t+1])
#     #     else:
#     #         print(tum[t])
#     # # print(a)
#     # print(num)
#     # print(e)
#     # # print(c)
        
        


k="string"
h=[]
for l in k:
    h.append(l)
print(h)
for _ in range(len(h)):
    h.pop()
print(h)