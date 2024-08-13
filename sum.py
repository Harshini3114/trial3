a = 143
b = len(str(a))
y=str(a)
k=0
for i in range (b):
    x=y[i]
    d=int(x)
    c=d**b
    k=k+c

if k==a:
    print("it is an armstrong number")
else:
    print("It is not an armstrong number")
    
    
    
    
    
    
