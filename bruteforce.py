from datareader import getAndFormatData
from decorator import chrono_decorator
from itertools import combinations


PATH = "data\\dataset0.csv"

CREDIT = 500


def best_portfolio_bruteforce(budget, actions, best_actions = []):
    if actions:
        # Cas où l'on ne selectionne pas l'action en cours
        list0, profit0 = best_portfolio_bruteforce(budget, actions[1:], best_actions)
        action = actions[0]
        actionCost = action[1]
        # Cas où l'on selectionne l'action en cours (le budget le permettant)
        if actionCost <= budget:
            budget1 = budget - actionCost
            best_actions1 = best_actions + [action]
            list1, profit1 = best_portfolio_bruteforce(budget1, actions[1:], best_actions1)
            if profit1 > profit0:
                return list1, profit1
        return list0, profit0
    else:
        best_profit = sum([a[2] for a in best_actions])
        return best_actions, best_profit






def best_portfolio(budget, actions):
    """
    teste toutes les combinaisons possibles et renvoie la liste des actions la
    plus rentable dans le budget imparti
    """

    range = len(actions)
    best_profit = 0
    best_actions = None
    best_cost = 0
    while range > 1:
        print("Range : " + str(range))
        combinaisons = combinations(actions, range)
        range -= 1
        for combinaison in combinaisons:
            profit = 0
            cost = 0
            for action in combinaison:
                cost += action[1]
                profit += action[2]
            if cost <= (CREDIT * 100) and profit > best_profit:
                best_profit = profit
                best_actions = combinaison
                best_cost = cost


    return best_actions, best_profit

@chrono_decorator
def main(*args, **kwargs):
    return best_portfolio_bruteforce(*args, **kwargs)

if __name__ == '__main__':
    # Ouvre le fichier csv et renvoi une liste d'actions sous forme de tuples
    # (nom, prix, profit généré)
    # Valeurs en centimes pour travailler avec des entiers
    actions = getAndFormatData(PATH)

    print("lancement avec ", len(actions), "actions", "(" + PATH + ")")

    best_actions, best_profit = main(CREDIT * 100, actions)

    cost = 0
    print("Meilleure combinaison d'actions : ")
    for action in best_actions:
        print(action[0])
        cost += action[1]
    print("Coût total : ", cost / 100 , "€")
    print("Bénéfice total : ", best_profit / 100, "€")
