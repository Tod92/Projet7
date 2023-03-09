import csv

def isStrictPositive(element):
    """
    Verifie que l'objet est un nombre et que ce dernier superieur à zero
    """
    try:
        return float(element) > 0
    except ValueError:
        return False

def toCents(tupleElement):
    """
    Transforme le tuple reçu au format voulu (nom, cout, profit)
    avec cout et profit entiers en centimes
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
    with open(path,"r") as csvfile:
        reader = csv.reader(csvfile)
        # Retire l'en-tete et les actions ayant pour cout 0
        actions = [tuple(e) for e in reader if isStrictPositive(e[1])]
        actions = list(map(toCents, actions))
    return actions

if __name__ == '__main__':
    actions = getAndFormatData("data\\dataset1.csv")
    for a in actions:
        print(a)
