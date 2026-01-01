text=input("enter your text: ")
a=0x67452301
b=0xEFCDAB89
c=0x10325476
d=0x98BADCFE
e=0xC3D2E1F0

for ch in text:
    n=ord(ch)
    a=(a+n)& 0xFFFFFFFF
    b=(b^a)& 0xFFFFFFFF
    c=(c+b)& 0xFFFFFFFF
    d=(d^c)& 0xFFFFFFFF
    e=(e+d)& 0xFFFFFFFF

digest='%08x%08x%08x%08x%08x'%(a,b,c,d,e)
print("Sha 1:",digest)