# Python3,mvs, 2017-09-27

list1 = []
while True:
    try:
        x = float(input("X-coordinate bitte:") or 0)
        y = float(input("Y-coordinate bitte:") or 0)
        z = float(input("Z-coordinate bitte:") or 0)
    except ValueError:
        print("Eingabe beendet.")
        break
    koordinate = (x, y, z)
    list1.append(koordinate)
    print(str(koordinate) + " was saved.")
print("Final List:")
print(list1)
# Third Value(i.e., z) in second data set
# print(list1[1][2])
