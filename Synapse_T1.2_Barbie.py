#PS
lst = ['0001', '0011', '0101', '1011']
new_lst = []
temp = []
a=0

for s in lst:
    i = int(s,2)
    new_lst.append(i)
print(new_lst)

new_lst.sort(reverse=True)
print(new_lst)
l = len(new_lst)

"""def Cons(li):
    return li == list(range(max(l)+1, min(l)))
b = Cons(new_lst) """

#if (b==False) :
while l>2:
            a = new_lst[l-1] + new_lst[l-2]
            new_lst.remove(new_lst[l-1])
            l = len(new_lst)
            new_lst.remove(new_lst[l-1])
            new_lst.append(a)
            print(new_lst)
"""else:
    if (l%2 == 0):
        for i in range(1, l):
            s1 = new_lst[i-1]+new_lst[l-i]
            temp.append(s1)
        print(temp)
"""

d = abs(new_lst[0] - new_lst[1])
print("Least difference between Barbie and Ken is",d)