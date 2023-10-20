
import math
from math import sqrt

#exercice 2

#Q1
def cherche(chaine: str, lettre: str)->bool:
    for i in range(len(chaine)):
        if chaine[i] == lettre:
            return True
    return False
        


def cherche_v2(chaine: str, lettre: str):
    for k in chaine:
        if k == lettre:
            return True
    return False

#Q2
def cherche2(chaine: str, lettre: str)->list:
    occurence = []
    for i in range(len(chaine)):
        if chaine[i] == lettre:
            occurence.append(i)    
    return occurence


#Q3 : Oui


#Exercice 3

def voy(phrase: str)->int:
    liste_voy = 'aeiouy'
    nombres_occurences = 0 
    for i in range(len(phrase)):
        if phrase[i] in liste_voy:
            nombres_occurences = nombres_occurences + 1
    return nombres_occurences


#Exercice 4
def modif_liste(L: list)->list:
    liste_oppose = []
    for i in range(len(L)):
        if L[i]%2 == 0:
            liste_oppose.append(-L[i])
        else:
            liste_oppose.append(L[i])
    return liste_oppose


#Exercice 5

def Un(N: int, u0: int)->list:
    u = u0
    print(u)
    liste_u = [u0]
    for i in range(1,N+1):
        u = u - 3*(i-1)
        liste_u.append(u)
    return liste_u

#Q2
def sommeUn(n:int, u0: int)->int:
    somme = 0
    L = Un(n,u0)
    for i in range(len(Un(5,1))):
        somme = somme + L[i]
    return somme


#Q3
def rang(u0:int)->int:
    u = u0
    n = 0
    while u>=0:
        u = u - 3*n
        n = n + 1
    return n  


#Exercice 6

def maxi(L:list)->list:
    maxi = L[0]
    for i in range(0,len(L)):
        if maxi < L[i]:
            maxi = L[i]
    occurences = 0
    for i in range(0,len(L)):
        if L[i] == maxi:
            occurences = occurences + 1
    return maxi, i, occurences


def distance(pt: tuple)->int:
    origine = (0,0)
    distance_abscisse = (pt[0]-origine[0])**2
    distance_ordonnee = (pt[1]-origine[1])**2
    distance = sqrt(distance_abscisse + distance_ordonnee)
    return distance

def dist_maxi(L:list)->int:
    origine = (0,0)
    distances_maxi_abscisse = (L[0][0] - origine[0])**2
    distance_maxi_ord = (L[0][1] - origine[1])**2
    distance_maxi = sqrt(distances_maxi_abscisse + distance_maxi_ord)
    for i in range(0,len(L)):
        distances_maxi_abscisse_provisoire = (L[i][0] - origine[0])**2
        distance_maxi_ord_prv = (L[i][1]-origine[1])**2
        distance_maxi_provisoire = sqrt(distances_maxi_abscisse_provisoire + distance_maxi_ord_prv)
        if distance_maxi < distance_maxi_provisoire:
            distance_maxi_provisoire = distance_maxi
    return distance_maxi

#Ex 7




