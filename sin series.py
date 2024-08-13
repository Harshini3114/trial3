a = int(input())
x = x*(3.14/180)
fac=-1
sinx=x
for i in range(3,7,2):
    fac=(-1)*fac*(i-1)
    sinx=sinx+(x**i/fac)
print(sinx)



