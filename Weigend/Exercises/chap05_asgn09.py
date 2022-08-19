#Python3,mvs, 2017-09-27
#Chapter 5 / Assignment 9 / Character print

ascii_numbers=[i for i in range(65,91)]
doublets=[]
for i in ascii_numbers :
    for j in ascii_numbers :
        #print(chr(j)+chr(i)+", ", end='')
        doublets.append(chr(j)+chr(i))

print(doublets)
print("Ende des Programms") 
