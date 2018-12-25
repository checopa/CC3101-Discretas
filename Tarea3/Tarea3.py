import networkx as nx;


#Crea un grafo donde los nodos son los actores
# y en las aristas tienen un tercer valor que es la pelicula
def crearGrafo(coleccion,actores):
    G=nx.MultiGraph()
    for j in range(len(coleccion)):
        for i in range(len(actores[j])):
            aux=i+1
            while(aux<len(actores[j])):
                G.add_edge(actores[j][i],actores[j][aux],coleccion[j])
                aux+=1
    return G


#Entrega todos los caminos entre inicio y meta
def dfs(G,inicio,meta):
    cam=[]
    stack = [(inicio, [inicio])]
    while stack:
        (vertice, path) = stack.pop()
        lista=list(G[vertice])
        for i in path:
            if i in lista:
                lista.remove(i)
        for next in lista:
            if next==meta:
                cam.append(path+[next])
            else:
                stack.append((next,path+[next]))
    return cam

#Calcula el camino mas corto desde A hasta Maryl Streep
# y luego el camino mas corto entre Maryl Streep y Kevin Bacon
# para luego unirlos y entregar el tamaño del camino.
def NroMinPeliculas(A, coleccion, actores):
        G = crearGrafo(coleccion, actores)
        x = dfs(G, A, 'Maryl Streep')
        aux = pelis(G, x)[0]
        x2 = dfs(G, 'Maryl Streep', 'Kevin Bacon')
        aux2 = pelis(G, x2)[0]
        final = unir(aux, aux2)
        return len(final)

#Dada una lista de actores, entrega las peliculas en comun que
#tienen entre todos ellos
def pelis(G,x):
    listapelis = []
    for i in x:
        listaux = []
        aux = i[:]
        for j in i:
            aux.remove(j)
            for k in aux:
                peli = peliencomun(G, j, k)
                if peli != 0 and peli not in listaux:
                    listaux.append(peli)
        listapelis.append(listaux)
    return listpequeña(listapelis)

#Une dos listas donde el ultimo elemento de la primera
#es igual al primero del segundo
# (No repite ese elemtno)
def unir(l1,l2):
    lista=[]
    for i in l1:
        lista.append(i)
    x=lista[len(lista)-1]
    for i in l2:
        if i!=x:
            lista.append(i)
    return lista


#Dado dos actores retorna la pelicula en comun
def peliencomun(G,act1,act2):
    for i,j in G[act2].items():
        if i==act1:
            for k in j.items():
                return k[0]
    return 0


#Dada una lista de maratones, entrega las de menor tamaño
def listpequeña(L):
    min=float('inf')
    ind=0
    for i in range(len(L)):
        if len(L[i])<min:
            min=len(L[i])
            ind=i
    listaux=[]
    for i in L:
        if len(i)==min and i not in listaux:
            listaux.append(i)
    return listaux

#Calcula el camino mas corto desde A hasta Maryl Streep
# y luego el camino mas corto entre Maryl Streep y Kevin Bacon
# para luego unirlos y retornar el camino
def UnaMaratonMinimal(A,coleccion,actores):
    G = crearGrafo(coleccion, actores)
    x = dfs(G, A, 'Maryl Streep')
    aux = pelis(G, x)[0]
    x2 = dfs(G, 'Maryl Streep', 'Kevin Bacon')
    aux2 = pelis(G, x2)[0]
    final = unir(aux, aux2)
    return final

#Calcula el camino mas corto desde A hasta Maryl Streep
# y luego el camino mas corto entre Maryl Streep y Kevin Bacon
# para luego unirlos y retornar el numero de todas las maratones minimales
def NroMaratonesMinimales(A,coleccion,actores):
    G = crearGrafo(coleccion, actores)
    x = dfs(G, A, 'Maryl Streep')
    aux = pelis(G, x)
    x2 = dfs(G, 'Maryl Streep', 'Kevin Bacon')
    aux2 = pelis(G, x2)
    lista=[]
    for i in aux:
        for j in aux2:
            lista.append(unir(i,j))
    return len(listpequeña(lista))
