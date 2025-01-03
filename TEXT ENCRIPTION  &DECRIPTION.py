def encript(st,key):
    g=""
    for i in st:
        if i==" ":
            g=g+" "
        else:
            if i in letters:
                i=ord(i)+key
                if i>122:
                    i=i-26
                g=g+chr(i)
    print(g)      
def decript(st,key):
    g=""
    for i in st:
        if i==" "
            g=g+" "
        else:
            if i in letters:
                i=ord(i)-key
                if i<97:
                    i=i+26
                g=g+chr(i)
    print(g)  
letters='abcdefghijklmnopqrstuvwxyz'
key=int(input("Enter the shift value"))
st=input("Enter the string to perform operations.").lower()
print("encript or decript")
i=input("e for encript and d for decript")
if i=='e':
    encript(st,key)
else:
    decript(st,key)
    
