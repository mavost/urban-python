#!/usr/bin/python #Linux shebang plus chmod to make executable
''' main - a small piece of code
'''
name=input('Name:')
print('Hallo ',name,' !', sep='')
height=float(input('Körpergröße[cm]:'))

bmi=0.0
#endless loop until break condition is reached
while True:
#repeat while bmi is poor
#while bmi<18.5 or bmi>=25.0:
#repeat ten times
#for i in range(1,11):
    weight=input('Gewicht[kg]:')
    if not len(weight):
        break
    try:
        bmi=float(weight)/height**2*10000
    except ValueError:
        print("Fehlerhafte Eingabe!")
        continue
    except ZeroDivisionError:
        print("Fehlerhafte Eingabe bei der Körpergröße!")
        height=float(input('Körpergröße[cm]:'))
        continue
    #alternativ round(BMI,2)
    #print(bmi)
    print('BMI:', '{:6.2f}'.format(bmi))
    if bmi>=25:
        print("Could be a sign of overweight. Please consult a doctor...")
    elif bmi<18.5:
        print("Could be a sign of starvation. Please consult a doctor...")
    else:
        print("Sounds healthy...")

print("End of calculation")
