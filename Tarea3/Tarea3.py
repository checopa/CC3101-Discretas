import networkx as nx;
import matplotlib.pyplot as plt


coleccion=["Eficiente y furioso 3: Dijkstra Drift","Mi papa es un grafo!","Discretas 4, una nueva esperanza"]
actores=[["Peibl Towers","Vim Diesel"],["Vim Diesel","Maryl Streep", "Andrea Lalancha"],["Andrea Lalancha","Kevin Bacon"]]


def crearGrafo(coleccion,actores):
    G=nx.MultiGraph()
    for j in range(len(coleccion)):
        for i in range(len(actores[j])):
            aux=i+1
            while(aux<len(actores[j])):
                G.add_edge(actores[j][i],actores[j][aux],coleccion[j])
                aux+=1
    return G




def NroMinPeliculas(A,coleccion,actores):
    G=crearGrafo(coleccion,actores)
    print(list(G.nodes()))
    print(list(G.edges()))
#def dijkstrachanta(G,nodoin,nodofin):


NroMinPeliculas("Peibl Towers",coleccion,actores)