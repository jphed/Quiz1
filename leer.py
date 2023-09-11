filetxt = open('datos.txt', 'r')
data = []
uno=0;dos=0;tres=0;cuatro=0;cinco=0;seis=0;siete=0;ocho=0;nueve=0;diez=0
c=0
for row in filetxt:
    data.append(row)
    if data[c] == '1\n':
        uno += 1
    if data[c] == '2\n':
        dos += 1
    if data[c] == '3\n':
        tres += 1
    if data[c] == '4\n':
        cuatro += 1
    if data[c] == '5\n':
        cinco += 1
    if data[c] == '6\n':
        seis += 1
    if data[c] == '7\n':
        siete += 1
    if data[c] == '8\n':
        ocho += 1
    if data[c] == '9\n':
        nueve += 1
    if data[c] == '10\n':
        diez += 1

    c += 1

print(f'1: {uno}\n2: {dos}\n3: {tres}\n4: {cuatro}\n5: {cinco}\n6: {seis}\n7: {siete}\n8: {ocho}\n9: {nueve}\n10: {diez}')


