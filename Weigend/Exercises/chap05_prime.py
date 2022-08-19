#Python3,mvs, 2017-09-27
#Chapter 5 / Prime numbers
import math 
final=int(input("Enter last number to check:"))

primes=[2]
b=0
for i in range(2,(final+1)):
    a=1
    for p in primes :
        #don't evaluate primes larger than sqrt of sample 
        if p > (int(math.sqrt(i))+1) : break
        b+=1
        #immediate exit after divisor found
        if not i%p : a*=0 ; break
    #all relevant primes checked, drop or add
    if a : primes.append(i)

print("Prime numbers after "+str(b)+" cycles:") 
print(primes)
