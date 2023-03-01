from openpyxl import Workbook
from openpyxl import load_workbook

PATH = "data.xlsx"
CREDIT = 500

def get_data(path):
    """
    Ouvre le fichier xlsx et renvoi une liste d'objets Action
    """
    wb = load_workbook(filename = PATH)
    ws = wb.active

    actions = []
    number = 0
    for row in ws.iter_rows():
        # On saute la ligne d'en tête
        if number > 0:
            name = row[0].value
            cost = row[1].value
            profit = row[2].value
            actions.append(Action(name, cost, profit))

        number += 1
    return actions


class Action:
    def __init__(self, name, cost, profit):
        self.name = name
        # Conversion en centimes pour travailler avec des entiers
        self.cost = int(cost * 100)
        self.profit = profit

    def __str__(self):
        result = str(self.name) + " : " + str(self.cost / 100) + "€ "
        result += str(self.profit) + "% sur 2 ans"
        return result

    @property
    def benefice(self):
        """
        Calcule et renvoi les benefices effectués sur 2 ans
        resultat en €
        """
        return int(self.cost * self.profit) / 100


if __name__ == '__main__':
    actions = get_data(PATH)

    bank = int(CREDIT * 100)
    purchase = []
    for action in actions:
        if bank >= action.cost:
            purchase.append(action)
            bank -= action.cost

    for action in purchase:
        print(action)
