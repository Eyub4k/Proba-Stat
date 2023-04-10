import numpy as np
import matplotlib.pyplot as plt
import math
#*********************************** 1.1 Loi Poisson *************************************************************

# On debute avec La loi de Poisson :

# Voici la fonction qui vas nous permettre de calculer la loi de poisson theorique :

def loiPoisson(landa,k):
    """Renvoie une probabilité, avec k et lambda en entree"""
    return (landa ** k * math.exp(-landa)) / math.factorial(k)

# creation d'une liste qui va nous permettre de stocker k fois avec landa qui vaut 1,10 ou 100 :
liste_poisson_theorique = []

#boucle qui nous permet d'appliquer la loi Poisson
for i in range(50):
    liste_poisson_theorique.append(loiPoisson(10,i))
#print(liste_poisson_theorique)


# Voici la loi poisson simuler avec la fonction de numpy, remplie dans une liste:

liste_poisson_simulee = np.random.poisson(10,1000)

#Creation de notre histogramme qui prendra les valeurs de la fonction numpy et une courbe qui prendra les valeurs theorique
plt.plot(liste_poisson_theorique, linewidth=2, color='r',label='Densité théorique')
plt.hist(liste_poisson_simulee, density=True, alpha=0.5, label='Données simulées')
plt.xlabel('k')
plt.ylabel('Probabilité')
plt.title('fonction de densitée : loi Poisson')
plt.legend()
plt.show()

# pour la fonction de repartition :

def fonctionRepartionPoissonTheor(landa,k):
    """Renvoie une probabilité, avec k et lambda en entree"""
    liste_r = []
    rep = loiPoisson(10,0)
    liste_r.append(rep)
    for i in range(30):
        rep = rep + loiPoisson(10,i+1)
        liste_r.append(rep)
    return liste_r

def fonctionRepartionPoissonSimu(landa,k):
    """Renvoie une probabilité, avec k et lambda en entree"""
    liste_r = []
    rep = 0
    for i in range(1000):
        rep = rep + np.random.poisson(10)
        liste_r.append(rep)
    return liste_r

# mes fonctions de repartition ne marchent pas, j'ai des histogrammes qui ne marchent pas

#*********************************** 1.1 Loi Binomiale *************************************************************

# Nous allons maintenant voir pour la loi binomiale

# debutons par la fonction de la loi binomiale theorique :

def loiBinomiale(n,p,k):
    """Renvoie une probabilité, avec k, p et lambda en entree"""
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) # math.comb permet de calculer le coefficient binomial

#liste qui permet d'appliquer la loi Binomiale pour different n

liste_Binomiale_theorique = []

#on remplie notre liste

for i in range(100):
    liste_Binomiale_theorique.append(loiBinomiale(50,0.2,i))

#on remplie une liste avec les proba trouvees avec la fonction de numpy

liste_Binomiale_simulee = np.random.binomial(50,0.2,100)

#Creation de notre histogramme qui prendra les valeurs de la fonction numpy et une courbe qui prendra les valeurs theorique
plt.plot(liste_Binomiale_theorique, linewidth=2, color='r',label='Densité théorique')
plt.hist(liste_Binomiale_simulee, density=True, alpha=0.5, label='Données simulées')
plt.xlabel('k')
plt.ylabel('Probabilité')
plt.title('fonction de densitée : loi Binomiale')
plt.legend()
plt.show()




#*********************************** 1.2 Loi Normale *************************************************************

# Nous allons voir la loi Normale, commencons par faire la fonction theorique :

def loiNormale(sigma,mu,x):
    """Renvoie une probabilité, avec sigma, mu et x en entree"""
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - mu) ** 2 / (2 * sigma ** 2))

#liste qui permet d'appliquer la loi normale pour different x
liste_Normale_theorique = []

#on remplie notre liste
for i in range(100):
    liste_Normale_theorique.append(loiNormale(math.sqrt(50*0.25),25,i))

#on remplie une liste avec les proba trouvees avec la fonction de numpy
liste_Normale_simulee = np.random.normal(25, np.sqrt(50 * 0.25),100)

#Creation de notre histogramme qui prendra les valeurs de la fonction numpy et une courbe qui prendra les valeurs theorique
plt.plot(liste_Normale_theorique, linewidth=2, color='r',label='Densité théorique')
plt.hist(liste_Normale_simulee, density=True, alpha=0.5, label='Données simulées')
plt.xlabel('x')
plt.ylabel('Probabilité')
plt.title('fonction de densitée : loi Normale')
plt.legend()
plt.show()



#*********************************** 1.2 Loi exponentielle  *************************************************************

#Nous allons voir maintenant la loi exponentiellen commencons par coder la fonction :

def loiExponentielle(landa,x):
    """Renvoie une probabilité pour la fonction de densite, avec lambda et x en entree"""
    return landa*(math.exp(-1*x))

#liste qui permet d'appliquer la loi exponentielle pour different x
liste_exponentielle_theorique = []

#on remplie notre liste
for i in range(1000):
    liste_exponentielle_theorique.append(loiExponentielle(0.5,i))

#on remplie une liste avec les proba trouvees avec la fonction de numpy
liste_exponentielle_simulee = np.random.exponential(0.5,1000)


#Creation de notre histogramme qui prendra les valeurs de la fonction numpy et une courbe qui prendra les valeurs theorique
plt.plot(liste_exponentielle_theorique, linewidth=2, color='r',label='Densité théorique')
plt.hist(liste_exponentielle_simulee, density=True, alpha=0.5, label='Données simulées')
plt.xlabel('x')
plt.ylabel('Probabilité')
plt.title('fonction de densitée : loi Exponentielle')
plt.legend()
plt.show()


def loiExponentielleRepartition(landa,x):
    """Renvoie une probabilité pour la fonction de repartition, avec lambda et x en entree"""
    return 1 - math.exp(-landa * x)

#liste qui permet d'appliquer la loi exponentielle pour different x en repartition
liste_exponentielle_theorique_repar = []

#on remplie notre liste
for i in range(100):
    liste_exponentielle_theorique_repar.append(loiExponentielleRepartition(0.2,i))

#Creation de notre histogramme qui prendra les valeurs avec la fonction de repartition :
plt.plot(liste_exponentielle_theorique_repar, linewidth=2, color='r',label='repartition théorique')
plt.xlabel('x')
plt.ylabel('Probabilité')
plt.title('fonction de repartition : loi Exponentielle')
plt.legend()
plt.show()

#*********************************** 2 Intervalle de confiance *************************************************************


# Nous allons coder l'  intervalle de confiance pour une variable aleatoire qui suit une loi Normale

# Pour commencer, nous allons coder la moyenne empirique Xn :

def moyenneEmpirique(tab): #elle prend en entree un tableau de Xi puis le code suit la formule sur le sujet :
    """Renvoie une moyenne, avec une liste des donnees qu'on veut etudier"""
    n = len(tab)
    x = 0
    for i in range(0, n):
        x = x + tab[i]
    return x / len(tab)

# puis on peut terminer par coder l'intervalle de confiance qui est sur le sujet :


def intervalleConfiance(tab, t, s):  # elle prend en entree t, le fractile de la loi Normale, s, l'ecart type, puis la liste des Xi
    """Renvoie une liste avec a gauche une valeur et a droite une autre valeur, avec t,s et une liste"""
    n = len(tab)

    ic_gauche = moyenneEmpirique(tab) - t * (s / (np.sqrt(n)))
    ic_droite = moyenneEmpirique(tab) + t * (s / (np.sqrt(n)))

    tab_ic = [ic_gauche, ic_droite]

    return tab_ic


#*********************************** 2.1 Temps de reaction *************************************************************

# temps de reaction :

# o = 0.25 u = 1

# tab_data, sont les valeurs du tableau pour le temps de reaction (on les a simuler avec le Professeur en tp, avec la boucle ci-dessous)

tab_data = []

for i in range(0, 20):
    tab_data.append(np.random.normal(1, (0.25)))


# moyenne empirique des data du dessus :
print("voici la moyenne empirique : ", (moyenneEmpirique(tab_data)))

#Tracons l'histogramme des echantillons ci-dessus :

plt.hist(tab_data, alpha=0.3, label='Données simulées')
plt.xlabel('Probabilité')
plt.title('Histogramme des echantillons')
plt.legend()
plt.show()

# pour determiner la fractile, on utilise les tables des fractiles

# intervalle de confiance pour alpha = 95%
print("intervalle de confiance pour alpha = 95% :",intervalleConfiance(tab_data,1.6449,0.20))

# intervalle de confiance pour alpha = 99%
print("intervalle de confiance pour alpha = 99% :",intervalleConfiance(tab_data,2.3264,0.20))

# On code l'ecart type empirique Sn :

def ecartTypeEmpirique(tab):
    """Renvoie l'ecart-type empirique, avec une liste en entree qui va permettre de calculer une moyenne empirique"""
    n = len(tab)
    s = 0
    m = moyenneEmpirique(tab)
    for i in range(0, n):
        s = s + (tab[i] - m) ** 2
    return s / n


# intervalle de confiance pour alpha = 95% en utilisant la variance empirique :
print("intervalle de confiance pour alpha = 95% en utilisant la variance empirique :",intervalleConfiance(tab_data,1.6449,ecartTypeEmpirique(tab_data)))

# intervalle de confiance pour alpha = 99% en utilisant la variance empirique :
print("intervalle de confiance pour alpha = 99% en utilisant la variance empirique :",intervalleConfiance(tab_data,2.3264,ecartTypeEmpirique(tab_data)))


#*********************************** 2.2 Estimation d'une Proportion *************************************************************


# estimation proportion / nous allons devoir estimer p :
# pour estimer notre proportion, nous devons verifier si n  > 30, np > 5 puis n(1-p) >= 4
# ici on a n =1000  et f = 637/1000 ici np > 5 et n > 30 donc n(1-p) >= 4 donc les conditions sont verifiés
# on va donc pouvoir estimer l'IC a 95% : IC = [f-(1/sqrt(n));f+(1/sqrt(n))]

n_proportion = 1000
f = 637 / n_proportion
IC_proportion_gauche = f - (1 / np.sqrt(n_proportion))
IC_proportion_droite = f + (1 / np.sqrt(n_proportion))

print("IC proportion a 95%: [", IC_proportion_gauche, ";", IC_proportion_droite, "]")