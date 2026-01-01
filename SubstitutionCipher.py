alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key=[]

msg=input("enter : ").lower()
key_word=input("Enter : ").lower()

for i in key_word:
    if i not in key:
        key.append(i)
for i in alphabet:
    if i not in key:
        key.append(i)

cipher=""
for i in msg:
    if i.isalpha():
        cipher+=key[alphabet.index(i)]
    else:
        cipher+=i
print("Cipher text",cipher)

plain=""
for i in cipher:
    if i.isalpha():
        plain+=alphabet[key.index(i)]
    else:
        plain+=i
print("Plain text",plain)
