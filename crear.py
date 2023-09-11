import random

filetxt = open('datos.txt', 'w')

for i in range(100):


    filetxt.write(f'{str(random.randint(1,10))}\n')


    
filetxt.close()
