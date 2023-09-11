f = open('emp.txt', 'r')

for row in f:
    textsplit = row.split(',')
    primer = int(textsplit[1]);segundo = int(textsplit[2]);tercero = int(textsplit[3])
    suma = primer + segundo+ tercero
    print(f'{textsplit[0]}: {suma}')