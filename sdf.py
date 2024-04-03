import math
a, b, e = map(int,input("Введите числа A, B, e: ").split())
#8(969)652-64-07- Самая лучшая Санечка в мире 
k=1
a=[0,0,0]
x=[0,0,0]
y=[0,0,0]
y[1]=b
x[1]=a
x[k]=(1/2)*(x[k-1]+y[k-1])
#мяу
while abs(x[n]-y[n])>e:
    k+=1
    k.append((1/2)*(x[k-1]+y[k-1]))
print(a[n])
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import math
a = str(input("Введите число: "))
if str(3) in a:
    b = "Да"
else:
    b = "Нет"
s = sum(map(int, str(a)))
c = int(str(a)[::-1])
print("Цифр в числе: ", int(len(str(a))),"\nСумма всех цифр в числе: ", s, "\nНаличие 3 в числе: ", b,"\nРазвернутый текст: ", c, int(str(a)).count(0)
