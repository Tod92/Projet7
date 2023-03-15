from datareader import getAndFormatData
from decorator import chrono_decorator
from itertools import combinations


PATH = "data\\dataset0.csv"

CREDIT = 500

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


if __name__ == '__main__':

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
