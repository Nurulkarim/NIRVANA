
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()  # multiple input taking at a time.
#         scores = list(map(float, line))
#         student_marks[name] = scores
        
#     query_name = input()
    
#     new_marks=student_marks[query_name]
#     a=sum(new_marks)/3
    
#     print("%.2f"%a)
    
# if __name__ == '__main__':
#     N = int(input())
#     a=[]
#     for _ in range(N):
#         command=input().split()  #split takes as a string
#         # command[1],command[2]=int(command[1]),int(command[2])
#         if command[0]=='insert':
#             a.insert(int(command[1]),int(command[2]))
#         if command[0]=='print':
#             print(a)
#         if command[0]=='remove':
#             a.remove(int(command[1]))
#         if command[0]=='append':
#             a.append(int(command[1]))
#         if command[0]=='sort':
#             a.sort()
#         if command[0]=='pop':
#             a.pop()
#         if command[0]=='reverse':
#             a.reverse()







# if __name__ == '__main__':
#     n = int(input())
#     integer_list = tuple(map(int, input().split()))
#     t=integer_list
#     print(hash(t))

            

