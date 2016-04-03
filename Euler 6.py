#difference between the sum of the first one hundred numbers squared and the sum of the first 100 square numbers

sqsum=0

sumn=0

for r in range(101):
  sumn+=r
  sqsum+=r**2

print((sumn**2)-sqsum)
