from itertools import product

# Teeme sisendist pythonile 2 täidetavad käsklust
seos1, seos2 = open('seossis.txt').read().replace('<<','<').replace('>>','>').split('\n')[0:2]
print(seos1, seos2)

# Leiame kõik seostega sobivad permutatsioonid a, b, c hulgast, mis kuuluvad hulka {0, 1, 2} kui need rahuldavad seoseid
sobib = [(a,b,c) for a,b,c in product([1,2,3], [1,2,3], [1,2,3]) if eval(seos1) and eval(seos2)]
print(len(sobib))

# Leiame tabelis kohal (i, j) sobiva seose
def otsusta(i,j):
    ulop = ['<<', '>>', '==', '<=', '>=']
    pyop = ['<', '>', '==', '<=', '>=']

    tests = []

    # Vaatame kõiki võimalikke seoseid ja lisame operaatori listi, kui see sobib kõikide arvukolmikutega
    for op in pyop:
        lisada = 0;
        for s in sobib:
            if eval('%d%s%d' % (s[i], op, s[j]))==True:
                lisada = 1
            else:
                lisada = 0
                break
        if lisada == 1:
            # print(op)
            tests.append(1)
        else:
            tests.append(0)

    # Tagastame esimese sobiva seose listist
    return ulop[tests.index(True)] if any(tests) else '??'

if len(sobib)==0:
    # Vastuolu kui pole ühtegi sobivat arvupaari
    print('VASTUOLU')
    # print('VASTUOLU', file=open('seosval.txt','w'))
else:
    print(otsusta(0,0)+ ' ' + otsusta(0,1) + ' ' + otsusta(0,2) + '\n' + otsusta(1,0)+ ' ' + otsusta(1,1) + ' ' + otsusta(1,2) + '\n' + otsusta(2,0)+ ' ' + otsusta(2,1) + ' ' + otsusta(2,2),file=open('seosval.txt','w'))
