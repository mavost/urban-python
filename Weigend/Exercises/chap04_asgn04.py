#Python3,mvs, 2017-09-27
#Chapter 4 / Assignment 4

try:
    isbn_in_s=input("Enter ISBN number to verify:")
except ValueError:
    print("Terminated - Bad Values:")
    exit()
if len(isbn_in_s) != 10:
    print("Terminated - ISBN must consist of 10 digits.")
    exit()

z_slice=list(isbn_in_s)
z_slice_n=[]

try:
    z_slice_n=[int(i) for i in z_slice[:9]]
    if z_slice[9].lower() == 'x':
        z_slice_n.append(10)
    else:
        z_slice_n.append(int(z_slice[9]))
except ValueError:
    print("Terminated - Number has bad format.")
    exit()

checksum=0
#for a in range(9):
#    checksum+=(a+1)*z_slice_n[a]
for a,z in enumerate(z_slice_n[:9]):
    checksum+=(a+1)*z
    print(a,z)
hash_val=checksum%11

print("Checksum is "+str(checksum)+" and hash value is " + str(hash_val))
      
if hash_val == z_slice_n[9]:
    print("ISBN Number " +isbn_in_s+" is valid.")
else :
    print("ISBN Number " +isbn_in_s+" is not valid.")
