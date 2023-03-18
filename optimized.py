from datareader import getAndFormatData
from decorator import chrono_decorator

PATH = "data\\dataset0.csv"
# PATH = "data\\dataset2.csv"

CREDIT = 500


@chrono_decorator
def best_portfolio(budget, actions):
    """
    actions : liste de tuples (nom, cout, profit sur 2 ans) valeurs en cents
    budget : valeur en €
    retourne best_actions, best_profit
    """
    # Initialisation de la matrice nbActions x budget (en euros)
    matrice = [[0 for y in range(budget + 1)] for x in range(len(actions) + 1)]
    for a in range(1, len(actions) + 1):
        for b in range(1, budget + 1):
            # Si le cout de l'action est inferieur au budget en cours de
            # traitement dans la matrice
            if actions[a-1][1] <= (b * 100):
                matrice[a][b] = max(actions[a-1][2] + matrice[a-1][((b * 100) -actions[a-1][1])//100], matrice[a-1][b])
            else:
                matrice[a][b] = matrice[a-1][b]

    best_profit = matrice[-1][-1]

    # Construction de la liste des meilleurs actions en lisant la matrice
    # dans le sens inverse
    best_actions = []
    x = budget
    y = len(actions)

    while x >= 0 and y >= 0:
        action = actions[y-1]
        actionCost = action[1]
        actionProfit = action[2]
        if matrice[y][x] == matrice[y-1][(x - actionCost)//100] + actionProfit:
            best_actions.append(action)
            # print("j'ai ajouté : ", action)
            x -= actionCost // 100
        y -= 1

    return best_actions, best_profit

def readable_best_portfolio(budget, actions):

    # Initialisation de la matrice nbActions x budget (en euros)
    matrice = [[0 for x in range(budget + 1)] for y in range(len(actions) + 1)]

    for y in range(1, len(actions) + 1):
        for x in range(1, budget + 1):
            bInCents = x * 100
            actionCost = actions[y-1][1]
            actionProfit = actions[y-1][2]
            caseDuDessus = matrice[y-1][x]
            if actionCost <= bInCents:
                matrice[y][x] = max(actionProfit + matrice[y-1][(bInCents-actionCost)//100], caseDuDessus)
            else:
                matrice[y][x] = matrice[y-1][x]


    best_profit = matrice[-1][-1]


    # Construction de la liste des meilleurs actions en lisant la matrice
    # dans le sens inverse
    best_actions = []
    x = budget
    y = len(actions)

    while x >= 0 and y >= 0:
        action = actions[y-1]
        actionCost = action[1]
        actionProfit = action[2]
        if matrice[y][x] == matrice[y-1][(x * 100 - actionCost)//100] + actionProfit:
            best_actions.append(action)
            # print("j'ai ajouté : ", action)
            x -= actionCost // 100
        y -= 1

    return best_actions, best_profit




if __name__ == '__main__':
    # Ouvre le fichier csv et renvoi une liste d'actions sous forme de tuples
    # (nom, prix, profit généré)
    # Valeurs en centimes pour travailler avec des entiers
    actions = getAndFormatData(PATH)

    print("lancement avec ", len(actions), "actions", "(" + PATH + ")")
    best_actions, best_profit = best_portfolio(CREDIT, actions)

    cost = 0
    print("Meilleure combinaison d'actions : ")
    for action in best_actions:
        print(action[0])
        cost += action[1]
    print("Coût total : ", cost / 100 , "€")
    print("Bénéfice total : ", best_profit / 100, "€")
