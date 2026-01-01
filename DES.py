def encry(msg,key):
    cipher=[]
    for i , char in enumerate(msg):
        m=ord(char)
        k=ord(key[i%len(key)])
        c=(m^k)+32
        cipher.append(str(c))
    return " ".join(cipher)

def decry(cipher,key):
    parts=cipher.split()
    text=""
    for i,part in enumerate(parts):
        c=int(part)-32
        k=ord(key[i%len(key)])
        text+=chr(c^k)
    return text

msg=input("Enter :")
key=input("Entyer :")

encrypted=encry(msg,key)
decrypted=decry(encrypted,key)

print("Encrypted :",encrypted)
print("Decrypted: ",decrypted)