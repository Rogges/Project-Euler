#find the scores of a list of names based on a scoring algorithm provided by Project Euler

file=open(filepath)

file1=file.read()

file3=file1.split('"')

#alpha_values contains the point scores of each individual letters

alpha_values={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

file4=[x for x in file3 if x!=',' and x!='']

file4.sort()

score=0

#for loop contains the scoring algorithm 

for name in file4:
    index=file4.index(name)+1
    score1=0
    for letter in name:
        score1+=alpha_values[letter]
    score2=index*score1
    score+=score2

print(score)
        
