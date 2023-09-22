import math
from random import randint
import random
import time
#Exercice 1
l1 = [i for i in range(5,81)]

l2 = [i for i in range(0,201) if i%10==0]

l3 = [n**2 + 3*n - 1 for n in range(0,30)]

l4 = [0]
first = 0
while first<10:
    first = first+0.5
    l4.append(first)
#print(l4)

alea = [randint(0,50) for k in range(20)]

alea2 = [alea[i] for i in range(len(alea)) if alea[i] % 2 == 0]

#Exercice 2
def permute(L: list)->bool:
    print(L)
    if len(L) >= 2:
        L[0],L[1] = L[1],L[0]
        print(L)
    else:
        print(f"votre liste {L} ne contient pas 2 éléments au moins")

#permute([2,3,4,5,'VISDHVSDH'])
#exercice 3
def f(x: int)->int or float:
    if x > 0:
        return 1/x
    elif x%3 == 0 and x<0:
        return x/3
    else:
        return x-1

#exercice 6

def pair(n: int)->list:
    liste = []
    for i in range(0, n+1):
        if i%2 == 0:
            liste.append(i)
    return liste

#exerice 7

def affiche(L: list):
    for i in range(len(L)):
        print(L[i])


def affiche_(L: list):
    for k in L:
        print(k)

def affiche2(L: list):
    for i in range(len(L)):
        print(f"A la position {i} on a {L[i]}")

#exercice 8 

def som_inverse(n: int)->int or float:
    if n == 0:
        raise ZeroDivisionError
    else:
        term = 1
        for i in range(2, n+1):
            term = term +  1/i
        print(term)
        return term

def seuil_n(A):
    term = 0
    n = 1
    while term<=A:
        term = term + 1/n
        n = n + 1
    return n-1


#exercice 9

def diviseurs(n:int)->list:
    liste_diviseurs = []
    for i in range(1,n+1):
        if n%i == 0:
            liste_diviseurs.append(i)
    return liste_diviseurs

def premier(n):
    if len(diviseurs(n)) == 2:
        return n
    else:
        return False

#exercice 10

#def recherche(L:list, elt: int)->bool:
    #if elt in L:
        #return L.index(elt)

#while True:
    #print(recherche([random.randint(0,30) for i in range(30)], random.randint(0,30)))
    #time.sleep(3)

def recherche(L: list, elt: int)->list:
    liste_occurences = []
    for i in range(len(L)):
        if elt == L[i]:
            liste_occurences.append(i)
    return liste_occurences
#while True:
    #print(recherche([random.randint(0,30) for i in range(30)], random.randint(0,30)))
    #time.sleep(3)

#exercice 11
def fibonacci(k):
    if k in {0, 1}:
        return k
    return fibonacci(k - 1) + fibonacci(k - 2)

liste_fibo = [fibonacci(k) for k in range(15)]
print(liste_fibo)



        
