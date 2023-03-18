import csv

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
    with open(path,"r") as csvfile:
        reader = csv.reader(csvfile)
        # Retire l'en-tete et les actions inférieures ou égales à 0
        actions = [tuple(e) for e in reader if isStrictPositive(e[1])]
        # Transforme le profit (%) en benefice (€)
        actions = list(map(gen_income, actions))
        # Transforme les valeurs en centimes afin de travailler avec des entiers
        actions = list(map(toCents, actions))

    return actions

if __name__ == '__main__':
    actions = getAndFormatData("data\\dataset0.csv")
    for a in actions:
        print(a)
