
#Genera todas las palabras posibles.
def generaTexto(n):
    listpal=[""]*(4**n)
    letras=["a","s","j","k"]
    lar=4**n
    seguir=True
    if n==0:
        return 1
    while(seguir):
        for i in range(4**n):
            listpal[i]=listpal[i]+letras[(i/(lar/4))%4]
        lar=lar/4
        if lar<4:
            seguir=False
    
    cont=0
    for i in listpal:
        if estaPal(i):
            cont+=1
    return cont

# Retorna True si la palabra esta en el lenguaje
# y False si la palabra no esta en el lenguaje.
def estaPal(s):
    if len(s)==0:
        return True
    if len(s)==1 and s=="a":
        return True
    if len(s)==2 and s=="sk":
        return True
    if len(s)==3 and s=="jaj":
        return True
    if s[0]=="a":
        return estaPal(s[1:])
    if (len(s)>1) and s[:2]=="sk":
        return estaPal(s[2:])
    if  (len(s)>2) and s[:3]=="jaj":
        return estaPal(s[3:])
    return False



# Crea una lista con la cantidad de palabras
# de largo n y menor que estan en el lenguaje
# y entrega la proporcion entre la cantidad de palabras
# y la cantidad total de palabras que se pueden formar.
def generaTextEf(n):
    pal=[0]*(n+1)
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    pal[0]=1
    pal[1]=1
    pal[2]=2    
    i=3
    while(i<=n):
        pal[i]=pal[i-1]+pal[i-2]+pal[i-3]
        i+=1
    return pal[n]/(4**n)