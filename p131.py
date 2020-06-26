start = 1
end = 1000000
prime=[]
num=[]
for val in range(start, end + 1):
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           prime.append(val)
print(prime)

for i in range (1,1000000):
  for j in range (1,1000000):
    for p in prime:
      if (i**3==((j**3)+(j**2)*p)):
        num.append(i)
print(num)

s=set(num)
l=list(s)
print(s)
print(l)
print(len(l))
