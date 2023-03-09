from datareader import getAndFormatData
from decorator import chrono_decorator

# PATH = "data\\dataset1.csv"
PATH = "data\\dataset2.csv"

CREDIT = 500


@chrono_decorator
def best_portfolio(budget, actions):
    """
    actions : liste de tuples (nom, cout, profit sur 2 ans)
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

    return matrice[-1][-1]

def readable_best_portfolio(budget, actions):

    # Initialisation de la matrice nbActions x budget (en euros)
    matrice = [[0 for y in range(budget + 1)] for x in range(len(actions) + 1)]

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

    return matrice[-1][-1]



if __name__ == '__main__':
    actions = getAndFormatData(PATH)
    print("lancement avec ", len(actions), "actions")
    print(readable_best_portfolio(CREDIT, actions))
    actions2 = actions[:500]
    print("lancement avec ", len(actions2), "actions")
    print(best_portfolio(CREDIT, actions2))
    actions3 = actions[:250]
    print("lancement avec ", len(actions3), "actions")
    print(best_portfolio(CREDIT, actions3))
    actions4 = actions[:50]
    print("lancement avec ", len(actions4), "actions")
    print(best_portfolio(CREDIT, actions4))
