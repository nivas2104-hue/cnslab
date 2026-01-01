def gcd(a,b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a 

p=int(input("enter p :"))
q=int(input("enter q :"))
n=p*q
phi=(p-1)*(q-1)
e=2
while gcd(e,phi)!=1:
    e=e+1
d=pow(e,-1,phi)
msg=input("enter txtt: ")


cipher=[] 
for c in msg:
    cipher.append(pow(ord(c),e,n))
print("Encrypted :",cipher)


plain=""
for c in cipher:
    plain+= chr(pow(c,d,n))
print("Decrypted :",plain)
