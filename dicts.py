import random
from pprint import pprint

budget = 23 # Kunden matar in detta via prompt

# Detta är ditt inventarie, se till att alltid ha en produkt som kostar 1 kr 
# För att kunna matcha vilken budget som helst.
produktlista = [
    {'namn': 'jenka', 'pris': 1},
    {'namn': 'hallon', 'pris': 8},
    {'namn': 'puffar', 'pris': 4},
    {'namn': 'nappar', 'pris': 3},
    {'namn': 'kofte', 'pris': 2},
    {'namn': 'zahremar', 'pris': 9},
]

# PROGRAMMET BÖRJAR FÖRST HÄR:
varukorg = [] # Kunden börjar såklart med en tom varukorg.

# Detta är bara en funktion som summerar priset för alla varor i en lista
def summeraVarukorg(lista):
    total = 0
    for sak in lista:
        total += sak['pris']
    return total


# Här börjar loopen
while (True):
    # Randomisera produktlista för att få till roligare varukorgar
    random.shuffle(produktlista)
    # 1 - Summera vad som redan finns i varukorgen
    summa = summeraVarukorg(varukorg)
    # 2 - Ta reda på om det finns budget kvar att handla för, bryt annars
    if (summa == budget):
        break
    # 3 - Iterera över produktlista (tänk på att den är randomiserad)
    for produkt in produktlista:
        # 4 - Se vad som står i iffen
        if (produkt['pris'] + summa <= budget):
            # Lägg till produkten i varukorg
            varukorg.append(produkt)
            # Efter att ha lagt till en vara, bryt for loopen
            # och återgå till while loopen
            break 

print('Din påse är klar och kostar {0} kr'.format(summa))
pprint(varukorg)
