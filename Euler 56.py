#maximum digit sum for n; n=a**b, 1>a>100, 1>b>100

list1=[]

for a in range(1,100):
  for b in range(1,100):
    c=a**b
    d=[int(i) for i in str(c)]
    list1.append(sum(d))
  
print(max(list1))
