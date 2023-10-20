

#EX1


#L1 par compréhension
L1 = [i/20 for i in range(21)]


L2 = [(i,i**2) for i in range(2,101)]


def somme_listes(L1,L2):
    final_list = []
    for k in range(len(L1)):
        final_list.append(L1[k] + L2[k])
    return final_list



def matrice(n:int):
    mat = []
    for i in range(n):
        mat.append([0 for i in range(n)])
    return mat


#EX2
def mini(L):
    mini_ = L[0]
    for i in range(0,len(L)):
        if mini_ > L[i]:
            mini_ = L[i]
    occurences = []
    for i in range(0,len(L)):
        if L[i] == mini_:
            occurences.append(i)
    return mini_,occurences


#EX3
def liste_Un(N):
    liste_termes = []
    u = 2
    liste_termes.append(u)
    for i in range(0,N):
        u = u*i + u 
        liste_termes.append(u)
    return liste_termes


def seuil(A:float):
    u = 2
    n = 0
    while u<A:
        u = u*n + u
        n = n + 
    return n


def somme_Un(N:int):
    liste = liste_Un(N)
    somme = 0
    for i in range(len(liste)):
        somme = somme + liste[i]
    return somme

#Partie B
import numpy as np
import matplotlib.pyplot as plt

#X = [i/10 for i in range(-100, 101)]
#Y = [np.cos(X[i]) for i in range(len(X))]
#Y_sin = [np.sin(X[i]) for i in range(len(X))]
#plt.plot(X,Y)
#plt.plot(X,Y_sin)
#plt.show()

#Ex5

def graphe1():
    T = [i/100 for i in range(0, 631, 1)]
    X = [np.cos(T[i])*(1-np.cos(T[i])) for i in range(len(T))]
    Y = [np.sin(T[i])*(1+np.cos(T[i])) for i in range(len(T))]
    plt.plot(X,Y)
    plt.axis('scaled')
    plt.show()


#Ex6 

def syracuse(u0,N):
    liste_syracuse = []
    u = u0
    liste_syracuse.append(int(u))
    for i in range(N):
        if u % 2 == 0:
            u = u/2
            liste_syracuse.append(int(u))
        else:
            u = 3*u + 1
            liste_syracuse.append(int(u))
    return liste_syracuse



def temps_de_vol(u0):
    u = u0
    liste_syracuse = []
    liste_syracuse.append(u)
    n = 0
    while u!=1:
        if u%2== 0:
            u = u/2
            liste_syracuse.append(int(u))
            n = n + 1
        else:
            u = 3*u + 1
            n = n + 1
            liste_syracuse.append(int(u))
    return n,liste_syracuse


def altitude(u0):
    temps = temps_de_vol(u0)
    return max(temps[1])

X = [i for in range(1,2001)]
Y = [temps_de_vol(i) for i in range(1,2001)]
plt.scatter(X,Y)
plt.show()
