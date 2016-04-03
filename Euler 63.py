#number of positive integers that are n digits long and can be expressed as the nth power of another number

list1=[]

for x in range(1,100):
  for y in range(1,100):
    z=x**y
    z1=[int(i) for i in str(z)]
    if len(z1)==y:
      list1.append(z)

print(len(list1))
