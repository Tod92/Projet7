from itertools import combinations
import csv

# Fichier de données d'actions au format CSV avec colonnes :
# Nom de l'action
# Coût de l'action en euros
# Profit généré par l'action sur 2 ans en %
PATH = "data\\dataset0.csv"

CREDIT = 500

# Partie DATA
def isStrictPositive(element):
    """
    Verifie que l'objet est un nombre et que ce dernier superieur à zero
    """
    try:
        return float(element) > 0
    except ValueError:
        return False

def gen_income(tupleElement):
    """
    Transforme le tuple reçu au format voulu :
    (nom, cout, profit) -> (nom, cout, income)
    avec income = benefice généré arrondi 2 chiffres après la virgule
    """
    result = list(tupleElement)
    # Passage str -> float
    result[1], result[2] = float(result[1]) , float(result[2])
    # Calcul de l'income
    result[2] = round(result[2] * result[1] / 100, 2)

    return tuple(result)

def toCents(tupleElement):
    """
    Transforme le tuple reçu au format voulu (nom, cout, profit)
    avec profit = benefice généré
    """
    result = list(tupleElement)
    for i in range(1,3):
        result[i] = int(float(tupleElement[i])*100)
    return tuple(result)


def getAndFormatData(path):
    """
    Ouvre le fichier csv et renvoi une liste d'actions sous forme de tuples
    (nom, prix, profit généré)
    Valeurs en centimes pour travailler avec des entiers
    """
    try:
        with open(path,"r") as csvfile:
            reader = csv.reader(csvfile)
            # Retire l'en-tete et les actions inférieures ou égales à 0
            actions = [tuple(e) for e in reader if isStrictPositive(e[1])]
            # Transforme le profit (%) en benefice (€)
            actions = list(map(gen_income, actions))
            # Transforme les valeurs en centimes afin de travailler avec des entiers
            actions = list(map(toCents, actions))

    # Ajout pour pouvoir lancer le script seul car le livrable demandé par
    # Openclassrooms est le fichier .py seul, maglré la consigne suivante :
    # " Le programme doit donc lire un fichier contenant des informations sur
    # les actions, explorer toutes les combinaisons possibles et afficher le
    # meilleur investissement."
    except FileNotFoundError:
        print("Fichier de données non trouvé")
        print("utilisation de la liste d'action par défaut")
        actions = [("Action-1", 2000, 100),
                   ("Action-2", 3000, 300),
                   ("Action-3", 5000, 750),
                   ("Action-4", 7000, 1400),
                   ("Action-5", 6000, 1019),
                   ("Action-6", 8000, 2000),
                   ("Action-7", 2200, 154),
                   ("Action-8", 2600, 286),
                   ("Action-9", 4800, 624),
                   ("Action-10", 3400, 918),
                   ("Action-11", 4200, 714),
                   ("Action-12", 11000, 990),
                   ("Action-13", 3800, 874),
                   ("Action-14", 1400, 14),
                   ("Action-15", 1800, 54),
                   ("Action-16", 800, 64),
                   ("Action-17", 400, 48),
                   ("Action-18", 1000, 140),
                   ("Action-19", 2400, 504),
                   ("Action-20", 11400, 2052)]
    return actions

#Partie Logique

# Version avec itertools cominations : abandonnée car overlapping et import ne
# permettant pas de visualiser l'intégralité de ce qui se passe
def best_portfolio(budget, actions):
    """
    teste toutes les combinaisons possibles et renvoie la liste des actions la
    plus rentable dans le budget imparti ainsi que le bénéfice associé
    """

    range = len(actions)
    best_profit = 0
    best_actions = None
    best_cost = 0
    while range > 1:
        # print("Range : " + str(range))
        combinaisons = combinations(actions, range)
        range -= 1
        for combinaison in combinaisons:
            profit = 0
            cost = 0
            for action in combinaison:
                cost += action[1]
                profit += action[2]

            if cost <= (budget * 100) and profit >= best_profit:
                # Cas ou le profit est égal au meilleur profit trouvé précedement
                if profit == best_profit and cost > best_cost:
                    continue
                else:
                    best_profit = profit
                    best_actions = combinaison
                    best_cost = cost


    return best_actions, best_profit

if __name__ == '__main__':
    # Ouvre le fichier csv et renvoi une liste d'actions sous forme de tuples
    # (nom, prix, profit généré)
    # Valeurs en centimes pour travailler avec des entiers
    actions = getAndFormatData(PATH)
    print("lancement avec ", len(actions), "actions")

    best_actions, best_profit = best_portfolio(CREDIT, actions)

    cost = 0
    print("Meilleure combinaison d'actions : ")
    for action in best_actions:
        print(action[0])
        cost += action[1]
    print("Coût total : ", cost / 100 , "€")
    print("Bénéfice total : ", best_profit / 100, "€")
