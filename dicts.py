
print("!!!!!!!! Dicts är bra för att hålla 'key -> value' par. I python ser dicten ut såhär:")

enDict = {"key": "value"}
print(enDict)

'''
NOTERA:
Varje key -> value par i en dict avgränsas med ':' <--
key : value
Numeriska key/values behöver ej "" tecken. Men strängar måste såklart ha.

1 : 10 <-- giltig
"hej" : "hejdå" <-- giltig
"hej" : hejdå <-- error

Du kan ha hur många key:value par du vill i en dict. 
'''


print('\n\n')
print('## SÅ! Nu när vi har en dict. Titta hur enkelt det är att plocka ut saker ur den. Men först vill jag använda dictens sanna "POWER" :D. Jag vill ha en lista med massa dicts i (precis som vi pratade om i telefon), varje dict har enkla "keys" så att jag kan läsa ut saker ur den...')

'''
Här har vi ett bra inventarie för produkter, du kan lägga till hur många "egenskaper" (dvs key:value par) som helst per dict i din lista.
#
Lista = []
Dict = {}
Lista med dicts = [{}, {}, {}]
'''

betterDict = [
    {'namn': 'jenka', 'pris': 20, 'vikt': 10},
    {'namn': 'nötter', 'pris': 10, 'vikt': 120},
    {'namn': 'salta s', 'pris': 2, 'vikt': 5},
]

print('\n\n')
print("!!!!!!!! Nu vill jag 'iterera' över denna lista med dicts (betterDict), för att printa ut info om varje produkt. DU hade också kunnat använda infon till annat än att bara printa ut... Jag kommer ge dig två exempel så du får se exakt hur!")

'''
    Raden nedan denna kommentar itererar över betterdict och lagrar varje dict-rad i "produktinfo" variabeln.

    Variablen skrivs över för varje iteration. SÅ i första varvet i iterationen kommer produktinfo vara den första produkten i din betterdict på rad 33,
    i andra varvet kommer produktinfo vara dicten på rad 34, osv...

    Som du ser, så lagrar jag namn, pris och vikt i kortare variabler i varje iteration, så att jag kan använda datat med korta fina namn.
    '''

for produktInfo in betterDict:
    namn = produktInfo['namn']
    pris = produktInfo['pris']
    vikt = produktInfo['vikt']
    print(
        "Här låg det en produkt som heter: {0} och kostar: {1} kr. Den väger {2} gram.".format(namn, pris, vikt))

# Vi kan iterera över vårt inventarie hur många gånger vi vill, man kan göra allt i en och samma for loop eller så kan man göra flera och göra småsaker i varje

# Här nedan vill jag till exempel summera priset för ALLA inventarier du har.
totalpris = 0
totalvikt = 0
for produktInfo in betterDict:
    pris = produktInfo['pris']
    vikt = produktInfo['vikt']
    totalpris += pris
    totalvikt += vikt

print('\n\n')
print("VISSTE DU: Att om man köper alla godisar du har i dina inventarier så skulle man få betala {0} kr och kånka hem en påse som väger {1} gram!".format(
    totalpris, totalvikt))

# Prova nu att lägga till fler produkter i betterDict. När du kör scriptet igen kommer du se att summeringen och den andra loopen automatiskt tar hand om dina nya produkter :D KUL VA? :D


'''
    Notera hur ENKELT man kan läsa ut saker ur dicts. För man kan alltid referera till KEY värdet för att få ut value. 

    Så om du har:
    person -> roll
    dict = { "Mahsa" : "Syster" }

    Så kan du få ut personens roll genom att be om dict['Mahsa']

    Du kan också vända på det
    roll -> person
    dict = { "Syster" : "Mahsa" }
    DÅ hade du helt enkelt bett om dict['Syster'] för att få ut Mahsa
'''
