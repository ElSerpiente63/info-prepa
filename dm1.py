import math as m
from math import sqrt
import matplotlib.pyplot as plt
#Exercice 1
def trinome(a:float, b:float, c:float)->int:
    delta = b**2 - 4*a*c
    if delta > 0:
        return "2", (-b+sqrt(delta))/2*a, (-b-sqrt(delta))/2*a #2 en str pour ne pas le confondre avec une solution de l'équation.
    elif delta ==  0:
        return "1", -b/2*a 
    else:
        return "0"

def trinomeC(a: float, b:float, c:float):
    delta = b**2 - 4*a*c
    if delta > 0:
        print(f"2 solution réelles, {(-b+sqrt(delta))/2*a, (-b-sqrt(delta))/2*a}")
    elif delta == 0:
        print(f"1 solution réelles,{-b/2*a}")
    else:
        print(f'2 solutions complexes {(-b+1j*sqrt(-delta))/2*a,(-b + 1j*sqrt(-delta)/2*a)}')

#Exercice 2

def suite(n: int)->list:
    u = 2
    liste = []
    liste.append(u)
    for i in range(n):
        u = 1.01 * u + 0.5
        liste.append(u)
    return liste

def sommeUn(n):
    liste = suite(n)
    somme = 0
    for i in range(len(liste)):
        somme = somme + liste[i]
    return somme

def depasseS(seuil: int)->int:
    n = 0
    u = 2
    S = suite(1)[0]*u  
    while S < seuil:
        for k in range(n):
            u = (u * 1.01 + 0.5)
            S = u*k
        n = n + 1 
    return n 
#Exercice 3

def liste_Un(n: int)->int:
    u = 4
    liste = [4*(-1)**i/(2*i + 1) for i in range(n)]
    return sum(liste)
print(liste_Un(10000))
print(liste_Un(100))
print(liste_Un(50))
#cela semble tendre vers pi (à vérifier)


def liste_Sn(n:int)->int:
    liste_pr = []
    for i in range(n+1): #on fixe i et on calcule n somme
        liste = []
        for k in range(i): #on introduit une nouvelle variable pour calculer les sommes
            liste.append(4*(-1)**k/(2*k + 1))
        liste_pr.append(sum(liste))
    del liste_pr[0] #pour supprimer le 0 qui venait bizarrement s'ajouter
    return liste_pr

def graphe(n:int):
    X = [k for k in range(n)]
    Y = [liste_Sn(n)[k] for k in X]
    plt.plot(X,Y,"o")
    plt.show()

graphe(51)

def precision(p:int)->int:
    n = 0
    S = 4
    while abs(S-m.pi) > 10**(-p):
        liste = [4*(-1)**k/(2*k + 1) for k in range(n)]
        S = sum(liste)
        n = n + 1
    return n
#Exercice 4 (non terminé)
def distance(pt1:tuple, pt2:tuple)->int:
    distance_ = sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)
    return distance_

def matrice(n:int, R:float)->list:
    color = [[0 for i in range(n)] for k in range(n)] #on crée une liste de liste ne contenant que des 0 et on remplace
    centre = color[round(n/2)][round(n/2)] #pas demandé mais on distingue les cas où n pair/impair
    coord_centre = (round(n/2), round(n/2))
    z = 0 #changement de valeur (ou non) fait 0 fois
    while z <= n**2:
        d = sqrt((n/2)**2 + (n/2)**2)
        for i in range(len(color)):
            for j in range(len(color[i])):
                d = sqrt((coord_centre[0] - i)**2 + (coord_centre[1] - j)**2)
                if (R*sqrt(z) < d <= R*sqrt(z+1)):
                    color[i][j] = 1
                    z = z + 1
                else:
                    z = z + 1
                    color[i][j] = 0
    return color 
#centre de la matrice [round(n/2)]
    

