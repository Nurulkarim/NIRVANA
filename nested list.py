
#I've tried for 2 days
if __name__ == '__main__':
    total_list=[]
    score_list=[]
    new_list=[]
    for _ in range(int(input())):  # will iterately take input name and score
        name = input()
        score = float(input())
        total_list.append([name,score])
        score_list.append(score)
    score_set = set(score_list)    # By making set ,same score will remove 
    new_list=list(score_set)
    new_list.sort(reverse=True)
    a=min(new_list)
    b=new_list.count(a)            #new_list er moddhe min(a) koita ase
    while b>1 :
        new_list.pop()
    new_list.sort()
    name_list=[]
    for name,score in total_list:  #unpacking name and score(making iterable boject into variable)
        if score==new_list[1]:     #if condition ekhane shobshomoy true hobe.
            name_list.append(name)
            name_list.sort()
    for new_name_list in name_list:#list print na kore iterably print korbe.
        print(new_name_list)
    



            