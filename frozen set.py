#frozen set
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x= set(a)
y=set(b)

count = 0
for i in range (len(x)):
    for j in range (len(y)):
        if a[i] == b[j]:
            count = count + 1
            
if count==0:
    print ("True")
else:
    print("False")
    
if count==0:
    print(frozenset(a))
    d = a+b
    print(frozenset(d))
else:
    c=set(a)-set(b)
    print(frozenset(c))
    d = a+b
    print(frozenset(d))



