#last 10 digits of the sum of a**a where a>=1 and a<=1000

x=range(1,1001)

y=[]

for i in x:
  y.append(i**i)

s=sum(y)

s1=[int(i) for i in str(s)]

s2=s1[len(s1)-10:]

for i in s2:
  ix=s2.index(i)
  s2[ix]=str(i)

print(''.join(s2))

