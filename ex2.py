import pandas as pd
import matplotlib.pyplot as plt
donnees = [
    ["Toyota", "Yaris", 2019, "janvier", "France", 1120],
    ["Peugeot", "208", 2019, "janvier", "France", 1090], #partie de la creation  de la donnes 
    ["Renault", "Clio", 2019, "janvier", "France", 930],
    ["Toyota", "Yaris", 2019, "février", "France", 980],
    ["Peugeot", "208", 2019, "février", "France", 850],
    ["Renault", "Clio", 2019, "février", "France", 780],
    ["Toyota", "Yaris", 2019, "mars", "France", 1270],
    ["Peugeot", "208", 2019, "mars", "France", 1030],
    ["Renault", "Clio", 2019, "mars", "France", 890],
    ["Toyota", "Yaris", 2019, "avril", "France", 1040],
    ["Peugeot", "208", 2019, "avril", "France", 980],
    ["Renault", "Clio", 2019, "avril", "France", 820],
    ["Toyota", "Yaris", 2019, "mai", "France", 1170],
    ["Peugeot", "208", 2019, "mai", "France", 1100],
    ["Renault", "Clio", 2019, "mai", "France", 920],
    ["Toyota", "Yaris", 2019, "juin", "France", 980],
    ["Peugeot", "208", 2019, "juin", "France", 890],
    ["Renault", "Clio", 2019, "juin", "France", 760]
]

colonnes = ["marque", "modele", "annee", "mois", "pays", "nombre_ventes"] #creation de les label de la header 
df = pd.DataFrame(donnees, columns=colonnes) # ajouter la cologne de la header a  la liste de donnes 

print(df.head()) # afficher le header de la liste par head()
print(df.info()) # pour afficher les informations on  fait .info()
print(df["nombre_ventes"].describe()) # afficher les desxription  d ' une descrption  d 'un  colone  

plt.figure(figsize=(10, 6)) # faire le talille de la figure
plt.hist(df["nombre_ventes"], bins=20, color="skyblue", edgecolor="black") # creation  de la histograme avec hoist(des parametre comme le coleur et  le binbd s)
plt.title("Histogramme des ventes")
plt.xlabel("Nombre de ventes")
plt.ylabel("Fréquence")
plt.show()

plt.figure(figsize=(8, 6))
plt.boxplot(df["nombre_ventes"], vert=False) # boxplot creation  de lui 
plt.title("Boxplot des ventes")
plt.xlabel("Nombre de ventes")
plt.show()

ventes_par_marque = df.groupby("marque")["nombre_ventes"].sum() # c'est comme une requette sql  c'est comme select sum(nbvnete) as nbv , marque  from data group  by  nbv 
print(ventes_par_marque)

meilleur_mois_par_marque = df.loc[df.groupby("marque")["nombre_ventes"].idxmax()]# df.loc electionner les lignes d 'appres sont indice 
print(meilleur_mois_par_marque[["marque", "mois", "nombre_ventes"]])

marque_max_ventes = ventes_par_marque.idxmax()#faire le affichage de la plsu  nombre de vente
# et  on utulise le  idmax quand on  fait un  totale de de sum  de categories et nous  afficher toujours la miellieur vente d'apres le idmax()
print(marque_max_ventes)

ventes_par_modele = df.groupby("modele")["nombre_ventes"].sum()
print(ventes_par_modele)

meilleur_mois_par_modele = df.loc[df.groupby("modele")["nombre_ventes"].idxmax()]
print(meilleur_mois_par_modele[["modele", "mois", "nombre_ventes"]])

modele_max_ventes = ventes_par_modele.idxmax()
print(modele_max_ventes)