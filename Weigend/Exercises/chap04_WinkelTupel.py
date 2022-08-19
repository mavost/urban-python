#Python3,mvs, 2017-09-27
import math

#get ranges to be pre-calculated
try:
    lower_a=float(input("Unterer Winkel:"))
    upper_a=float(input("Oberer Winkel:"))
    steps_a=int(input("Schritte:"))
except ValueError:
    print("Beendet - Values:")
    exit()
if not lower_a<upper_a or steps_a<1:
    print("Beendet - Ranges:")
    exit()
    
#generate intervals fill tuple, push to list
lista=[]
for i in range(steps_a+1):
    actual_a_deg=lower_a+i*(upper_a-lower_a)/steps_a
    actual_a_rad=actual_a_deg/180.0*math.pi
    tupel=(actual_a_deg,actual_a_rad,math.sin(actual_a_rad),math.cos(actual_a_rad))
    lista.append(tupel)
#convert list to tuple-array
tupela=tuple(lista)

#print(tupela)
print(lista)
#for i in tupela:
#    print("DEG: %6.2f SIN: %5.2f COS: %5.2f" % (i[0],i[2],i[3]))
