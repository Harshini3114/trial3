n = int(input())
d1={}
d2={}
d3={}
    
for i in range(n):
    name,m1,m2,m3=tuple(input().split())
    name=str(name)
    d1[name]=int(m1)
    d2[name]=int(m2)
    d3[name]=int(m3)
i=input()
avg=((d1[i]+d2[i]+d3[i])/3)
print(round(avg,2))    

