power_5=[]

#calculates numbers that can be expressed as the sum of their digits^5

for i in range(500000):
    digits=[int(x) for x in str(i)]
    fifth_power=[x**5 for x in digits]
    if sum(fifth_power)==i:
        power_5.append(i)

print(sum(power_5)-1) #removes the 1 that would be included by default
