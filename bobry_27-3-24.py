i=1 
e=0.001
y=[0.001,0]
x=int(input("Введите х: "))
y[1]=((1/2)*(y[i-1]+(x/y[i-1])))
while abs(y[i]-y[i-1])>e:
    i+=1
    y.append((1/2)*(y[i-1]+(x/y[i-1])))
print(y[i])
//////////////////////////////////////////
n = 1
e = int(input("e:"))
#8(969)652-64-07- Самая лучшая Санечка в мире 
a=[0.001,0]
a[1]=(n/(((n**2+1)**0.5)-((n**2)-1)**0.5))
#мяу
while abs(a[n]-a[n-1])>e:
    n+=1
    a.append(n/(((n**2+1)**0.5)-((n**2)-1)**0.5))
print(a[n])
////////////////////////////////////////////
n = 2
e = int(input("e:"))
#8(969)652-64-07- Самая лучшая Санечка в мире 
a=[0,0,0]
a[1]=0.5
a[2]=0.5*2/3
#мяу
while abs(a[n]-a[n-1])>e:
    n+=1
    a.append(a[n-1]*(1-1/n))
print(a[n])
/////////////////////////////////////////
import math
n=int(2)
e = int(input("e:"))
#8(969)652-64-07- Самая лучшая Санечка в мире 
a=[0,0,0]
a[1]=0.5
a[2]=0.5*2/3
#мяу
while abs(a[n]-a[n-1])>e:
    n+=1
    a.append(a[n-1]*(1+(-1**n)/math.factorial(n)))
print(a[n])