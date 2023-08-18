code = []
ec = []
dc = []
t = []
d1=1
d2=1
n = input("Enter number of codes ")

print("Enter a negative number to end sequence")
for i in range (int(n)):
    e = input("Enter code:")
    while (int(e)>=0):
        code.append(e)
        e = input()
    print(code)
    ec.append(code)
    code = []
print("Encoded codes:")
print(ec)

#print("Nuclear codes:")
for i in range (int(n)):
    t = ec[i]
    l = len(t)
    j=0
    while ((d1==1) and (d2==1)) and l>2 and (j<=l-3):
        a = int(t[j])
        b = int(t[j+1])
        c = int(t[j+2])
        d1 = b-a
        d2 = c-b
        if (d1 == 1) and (d2 == 1):
            #print(a,b,c)
            t.remove(str(a))
            t.remove(str(b))
            t.remove(str(c))
            #print("CP1")
        else:
            d1=1
            d2=1
            j += 1
        l = len(t)
        #print("CP2")
    dc.append(t)
print("Decoded Codes:")
print(dc)