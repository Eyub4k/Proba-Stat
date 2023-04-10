import numpy as np 
import matplotlib.pyplot as plt
import os 

#Fonctions utiles
def somme(n,x):
    """Renvoie la somme des x donné, avec n la taille de la liste de x, et une liste x en entree"""
    
    S = 0
    
    for i in range(n):
        S+=x[i]
    return S

def sommeCarre(n,x):
    """Renvoie la somme des x**2, avec n la taille de la liste de x, et une liste x en entree"""
    
    S = 0
    
    for i in range(n):
        S+=x[i]**2
    return S

def moyenne(x):
    """Renvoie la moyenne d'une liste de x, avec une liste x en entree"""
    
    S = 0
    
    for i in range(len(x)):
        S+= x[i]
    return S/len(x)

#Data


A = np.array([3500, 2800, 1300, 750, 300, 900, 1800, 3100]) #Altitude en m
Th = np.array([-15,-11,0,3,10,2,-2,-13]) #Temperature en hiver
Te = np.array([10,13,20,25,30,22,18,11]) #Temperature en ete

# Methode des moindres carre
def moindresCarres(y,x):
    """Renvoie les estimateurs a et b selon la méthode des Moindres Carres avec les listes x et y en entree"""
    
    n = len(x)
    a_c = 0
    
    for i in range(n):
        a_c += y[i]*x[i] 
    a_c = (a_c*n - somme(n,x)*somme(n,y))/((n*sommeCarre(n,x))-(somme(n,x)**2))
    b_c = (somme(n,y)/n)-(a_c*(somme(n,x)/n))
    
    return a_c,b_c

#Maximum de vraisemblance
def maxVraisemblance(y,x):
    """Renvoie les estimateurs a et b selon la methode Maximum de Vraisemblance avec les listes x et y en entree"""
    
    n = len(x)
    a_c = 0
    
    for i in range(n):
        a_c += y[i]*x[i]
    a_c = (1/n)*((a_c*n - somme(n,x)*somme(n,y))/(n*sommeCarre(n,x)-(somme(n,x)**2)))
    b_c = (1/n)*((somme(n,y)/n)-(a_c*(somme(n,x)/n)))
    
    return a_c,b_c


#Methode d'optimisation

def minJ(a,b,lx,ly):
    
    som = 0
    n = len(lx)
    
    for i in range(0,n):
        som += (a*lx[i]+b-ly[i])*(a*lx[i]+b-ly[i])
        
    return som

def Optimisation(ly,lx):
    """Renvoie les estimateurs a et b à l'aide des méthodes d'optimisation avec les listes x et y en entree"""
    
    a = 0
    b = 0
    a1 = a
    b1 = b
    som1 = 0
    som2 = 0
    ja = 0
    jb = 0
    lr = 0.5
    n = len(lx)
    res = 10**4
    
    while (res>10**(-3)):
        a1 = a
        b1 = b
        for i in range(0, len(lx)):
            som1 += lx[i]*(a*lx[i]+b-ly[i])
            som2 += (a*lx[i]+b-ly[i])
        ja = som1/n
        jb = som2/n
        som1 = 0
        som2 = 0
        a = a-lr*ja
        b = b-lr*jb
        res = minJ(a,b,lx,ly)-minJ(a1,b1,lx,ly)
        if(res<0):
            res = res*(-1)
            
    return a,b

#Qualite predictions
def RMSE(yc,y):
    """Root-mean-square deviation"""
    
    n = len(y)
    S = 0
    
    for i in range(n):
        S+= (yc-y)**2
    
    return np.sqrt(S/n)

def R2(yc,y):
    """Coefficient de détermination"""
    
    n = len(y)
    So = 0
    Se = 0
    moy = moyenne(y)
    
    for i in range(n):
        So += (y[i]-moy)**2
        Se += (yc[i]-moy)**2
        
    return Se/So



# #Exercice
os.system('cls')
a1,b1 = moindresCarres(Te,A)
a2,b2 = maxVraisemblance(Te,A)
a3,b3 = Optimisation(Te, A)
os.system('cls')
print("Moindres Carres\n")
print("a = ",a1,"\nb = ",b1)
print("\nMaximum Vraisemblance\n")
print("a = ",a2,"\nb = ",b2)
print("\nOptimisation\n")
print("a = ",a3,"\nb = ",b3)

input("Appuyez sur entrer pour continuer...")
os.system('cls')
x1 = np.random.rand(1,9)
y1 = []
y2 = []
y3 = []
for k in range(len(A)):
    y1.append(a1*A[k]+b1)
    y2.append(a2*A[k]+b2)
    y3.append(a3*A[k]+b3)
    
plt.plot(A,y1,"o", color="blue")
plt.ylabel("Température été en °C")
plt.xlabel("Altitude en m")
plt.title("Méthode Moidres Carrés")
plt.show()
plt.close()

plt.plot(A,y2,"o", color="red")
plt.ylabel("Température été en °C")
plt.xlabel("Altitude en m")
plt.title("Méthode Maximum de vraisemblance")
plt.show()
plt.close()

plt.plot(A,y3,"o", color="#008000")
plt.ylabel("Température été en °C")
plt.xlabel("Altitude en m")
plt.title("Méthode d'optimisation")
plt.show()

plt.close()
input("Appuyez sur entrer pour continuer...")
os.system('cls')
a1,b1 = moindresCarres(Th,A)
a2,b2 = maxVraisemblance(Th,A)
a3,b3 = Optimisation(Th, A)


x1 = np.random.rand(1,9)
y1 = []
y2 = []
y3 = []
for k in range(len(A)):
    y1.append(a1*A[k]+b1)
    y2.append(a2*A[k]+b2)
    y3.append(a3*A[k]+b3)
    
plt.plot(A,y1,"o", color="blue")
plt.ylabel("Température hiver en °C")
plt.xlabel("Altitude en m")
plt.title("Méthode moindres carrés")
plt.show()
plt.close()

plt.plot(A,y2,"o", color="red")
plt.ylabel("Température hiver en °C")
plt.xlabel("Altitude en m")
plt.title("Méthode maximum de vraisemblance")
plt.show()
plt.close()

plt.plot(A,y3,"o", color="#008000")
plt.ylabel("Température hiver en °C")
plt.xlabel("Altitude en m")
plt.title("Méthode d'optimisation")
plt.show()
plt.close()

