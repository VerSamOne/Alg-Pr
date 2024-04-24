#8 
n=int(input("Введите n:"))
a=0
for i in range(2, n//2+1):
    if n%i==0:
        a+=1
if a<=0:
    print("Число простое")
else:
    print("Число сложное")
  #
