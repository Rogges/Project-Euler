

upper=1000000 #upper bound for testing

list1=[] #contains numbers that have the same digits between the 1st,2nd,3rd,4th,5th, and 6th multiples


#runs through the test range defined by upper
#intersect finds the integers of intersection between the multiples
#if the length of intersect and x1 match up, then the same digits comprise all 6 multiples

for x in range(upper):
    twox=str(2*x); threex=str(3*x); fourx=str(4*x); fivex=str(5*x); sixx=str(6*x); x1=str(x)
    z1=[];z2=[];z3=[];z4=[];z5=[];z6=[]
    z1.extend(x1);z2.extend(twox);z3.extend(threex);z4.extend(fourx);z5.extend(fivex);z6.extend(sixx)
    intersect=set(z1).intersection(z2,z3,z4,z5,z6)
    if len(intersect)==len(x1):
        list1.append(x)
