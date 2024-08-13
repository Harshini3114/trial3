n = int(input())
print(2)
print(3)
print(5)
print(7)
i,count=2,1
while count<=n-4:
    if i%2!=0:
        if i%3!=0:
            if i%5!=0:
                if i%7!=0:
                    print(i)
                    count=count+1
    i=i+1
    
