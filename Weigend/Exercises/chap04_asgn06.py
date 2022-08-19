#Python3,mvs, 2017-09-27
#Chapter 4 / Assignment 6

tliste=[]
while True:
    try:
        name=str(input("Enter Name:"))
        if not name:
            print("Proceed after no entry.")
            break
        number=int(input("Enter Number:"))
        tliste.append((name,number))
    except ValueError:
        print("Proceed after bad or no entry.")
        break
if not tliste :
    print("Terminated - Missing Data.")
    exit()

print("Phone List of this week:") 
for a,entry in enumerate(tliste):
    print("Entry "+str(a+1)+": " + entry[0] + "\t" + str(entry[1]))

