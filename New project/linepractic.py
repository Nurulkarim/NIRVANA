"""
[list]    (tuple)    {set}           {dict}
append     count     intersection
clear      index     union
copy                 issubset
count                issuperset
extend
index
insert
pop
remove
reverse
sort

"""



n=input('enter the value:').split()
n[0],n[-1]=int(n[0]),int(n[-1])
print(n[0],n[-1])
# if operator=='+':
a=n[0]+n[-1]
print(f"{n[0]} + {n[-1]} = {a}")

