from datareader import getAndFormatData
from decorator import chrono_decorator

#PATH = "data\\actions.xlsx"
PATH = "data\\dataset1.csv"
CREDIT = 500


@chrono_decorator
def best_portfolio(budget, actions):
    """
    budget en euros
    actions : liste de tuples (nom, cout, profit sur 2 ans) en centimes
    """
    # Initialisation de la matrice nbActions x budget (en euros)
    matrice = [[0 for y in range(budget + 1)] for x in range(len(actions) + 1)]

    for a in range(1, len(actions) + 1):
        for b in range(1, budget +1):
            # Si le cout de l'action est inferieur au budget en cours de
            # traitement dans la matrice
            if actions[a-1][1] <= (b * 100):
                matrice[a][b] = max(actions[a-1][2] + matrice[a-1][(b*100-actions[a-1][1])//100], matrice[a-1][b])
            else:
                matrice[a][b] = matrice[a-1][b]

    return matrice[-1][-1]

# def readable_best_portfolio(budget, actions):
#     """
#     budget en euros
#     actions : liste de tuples (nom, cout, profit sur 2 ans)
#     """
#     # Initialisation de la matrice nbActions x budget (en euros)
#     matrice = [[0 for y in range(budget + 1)] for x in range(len(actions) + 1)]
#
#     for a in range(1, len(actions) + 1):
#         for b in range(1, budget +1):
#             # Si le cout de l'action est inferieur au budget en cours de
#             # traitement dans la matrice
#             bInCents = b * 100
#             actionCost = actions[a-1][1]
#             actionProfit = actions[a-1][2]
#             if actionCost <= bInCents:
#                 matrice[a][b] = max(actionProfit + matrice[a-1][(bInCents-actionCost)//100], matrice[a-1][b])
#             else:
#                 matrice[a][b] = matrice[a-1][b]
#
#     return matrice[-1][-1]


if __name__ == '__main__':
    actions = getAndFormatData(PATH)
    print(best_portfolio(500, actions))
