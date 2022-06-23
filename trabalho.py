import math
import numpy as np
import matplotlib.pyplot as plt

key = 0

print('Trabalho Computacional\nEmanuel Ávila Cruz Pires\nmatricula: 540286\n\n')
while key == 0:
   print('Escolha uma questão:\n\n 0 - sair')
   resp = input('-> ')
   resp = int(resp)
   if resp == 1:
       print('Questão 1 - Calcular medida Euclidiana entre dois pontos em um plano: \n')
       # recebe os valores que servirão de coordenada
       c_x = int(input('Digite a coordenada X: '))
       c_y = int(input('Digite a coordenada Y: '))
       c_x2 = int(input('Digite a coordenada X2: '))
       c_y2 = int(input('Digital a coordenada Y2: '))

       calc = math.sqrt(math.pow((c_x - c_x2), 2) + math.pow((c_y - c_y2), 2))

       print('O valor da soma Euclidiana e: {}'.format(calc))

       key = 0
   elif resp == 2:
       print('Questão 2 - Determine o ponto máximo da função: \n f(x) = (sen(pi * x) / x ')
       x = float(input('Digite a coordenada X'))

       y = np.sin((np.pi * x )) / x
       # y = x ** 3
       #y = 1 / (1 + np.exp(-x))

       plt.plot(x, y, color="blue", linewidth=3.0)
       plt.title("grafico senoide da funcao Y: ")
       plt.savefig("teste.png")
       plt.show()

       key = 0

   elif resp == 3:
       print('Questão 3 - Escreva as segintes matrizes: \n 10I[3][3] = {10,0,0,0,10,0,0,0,10}\n I[2][2] = {1,0,0,1}\n')

       matriz1 = [[0, 0], [0, 0]]
       matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

       for l in range(3):
          for m in range(3):
            matriz2[l][m] = int(input(f'digite um valor para matriz 3x3[l, m]: '))
       for n in range(2):
           for o in range(2):
               matriz1[n][o] = int(input(f'digite um valor para matriz 2x2[n, o]: '))

       print('Matriz 2x2: {}'.format(matriz1))
       print('Matriz 3x3: \n  {}'.format(matriz2))

       key = 0

   elif resp == 4:
       print('Questão 4 - Execute as seguintes portas lògicas: \n C = A && B\n C = A || B')
       key = 0

   elif resp == 0:
       key = 1

   else:
       print('Questão não encontrada!')

