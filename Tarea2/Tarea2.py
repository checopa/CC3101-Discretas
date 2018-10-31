def generaTexto(n):
    listpal=[""]*(4**n)
    letras=["a","s","j","k"]
    lar=4**n
    seguir=True
    while(seguir):
        for i in range(4**n):
            listpal[i]=listpal[i]+letras[(i/(lar/4))%4]
        lar=lar/4
        if lar<4:
            seguir=False
    listleng=buscpal(listpal)
    return (len(listleng)/(4.0**n))

def estaPal(s):
    i=0
    while(i<len(s)):
        if s[i]=="a":
            i+=1
            if(i>=len(s)):
                break
            else:
                continue
        if (s[i]=="j" and i<(len(s)-2)):
            if s[i+1]=="a" and s[i+2]=="j":
                i+=3
                if(i>=len(s)):
                    break
                else:
                    continue
            else:
                return False
        if (s[i]=="s" and i<(len(s)-1)):
            if s[i+1]=="k":
                i+=2
                if(i>=len(s)):
                    break
            else:
                return False
        else:
            return False
    return True

def buscpal(L):
    lista=[]
    for i in L:
        if estaPal(i):
            lista.append(i)
    return lista

