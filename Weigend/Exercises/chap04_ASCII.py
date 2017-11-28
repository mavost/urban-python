#Python3,mvs, 2017-09-27
list1=[]

dict1={}
for i in range(0,128):
    list1.append(i)
    dict1[i]=bytes([i])
#print(list1)
#print(bytes(list1))
for a in dict1:
    print(str(a)+ " : " + str(dict1[a])+"\n")

