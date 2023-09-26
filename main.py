import random

# Emplacement de Xavier Dupont de Ligonnès (caché dans une ville fictive)
emplacement_cible = random.choice(["Paris", "Marseille", "Lyon", "Bordeaux", "Nantes", "Toulouse"])

essais_restants = 3  # Nombre d'essais maximum

print("Bienvenue dans le jeu pour trouver Xavier Dupont de Ligonnès !")
print("Xavier Dupont de Ligonnès est caché dans une ville française. Vous avez 3 essais pour le trouver.")

while essais_restants > 0:
    print(f"Il vous reste {essais_restants} essais.")
    supposition = input("Entrez le nom de la ville où vous pensez qu'il se cache : ").strip().capitalize()

    if supposition == emplacement_cible:
        print(f"Félicitations ! Vous avez trouvé Xavier Dupont de Ligonnès à {emplacement_cible} !")
        break
    else:
        print("Ce n'est pas la bonne ville.")
        essais_restants -= 1

if essais_restants == 0:
    print(f"Dommage ! Xavier Dupont de Ligonnès était caché à {emplacement_cible}. Vous avez épuisé tous vos essais.")
