from openpyxl import Workbook
from openpyxl import load_workbook

PATH = "data.xlsx"

class Action:
    def __init__(self, name, cost, profit):
        self.name = name
        self.cost = cost
        self.profit = profit

def print_actions(actions):
    for action in actions:
        print(action.name, str(action.cost) + "€", str(action.profit) + "% sur 2 ans")

def calcul_profit(actions):
    """
    Liste d'actions en entrée
    Calcule et renvoi les benefices effectués sur 2 ans
    """
    result = 0
    for action in actions:
        result += (action.cost / 100) * action.profit
    return result


if __name__ == '__main__':

    wb = load_workbook(filename = PATH)
    ws = wb.active

    actions = []
    number = 0
    for row in ws.iter_rows():
        if number > 0:
            name = row[0].value
            cost = row[1].value
            profit = row[2].value
            actions.append(Action(name, cost, profit))

        number += 1
    print_actions(actions)
    print(calcul_profit([actions[2]]))
