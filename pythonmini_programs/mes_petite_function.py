def liste_de_valeur():
    liste_de_valeur=[]
    for value in range(0,5):
       print("enter a new value:")
       valeur_temporaire=input()
       liste_de_valeur.append(valeur_temporaire)
    print(liste_de_valeur)
def convertiseur_de_second(seconde):
    
    x_minute=seconde/60
    x_heurs=seconde/3600
    x_jour=seconde/86400
    x_mois=seconde/2678400
    x_year=seconde/32140800
    print(x_heurs)
    
def table_de_7():
    for i in range(0,12):
        produit=i*7
        if produit%3==0:
            print(str(produit)+"*")
        else:
            print(produit)
def suite_detoile():
    etoile=""
    for i in range(1,12):
            etoile+="*"
            print(str(etoile))
suite_detoile()   
        
            
    
