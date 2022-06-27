import math
import numpy as np
import matplotlib.pyplot as plt

key = 0

print('\n\nTrabalho Computacional\nEmanuel Ávila Cruz Pires\nmatricula: 540286\n\n')
while key == 0:
  print('\n\n1 - \n2 - \n3 - \n4 - \n0 - sair\n')
  print('Escolha uma questão: ')
  resp = input('-> ')
  resp = int(resp)
   
  if resp == 1:

        print('\nQuestão 1 - Calcular medida Euclidiana entre dois pontos em um plano: \n')
        # recebe os valores que servirão de coordenada
        c_x = [0, 0]
        c_y = [0, 0]

        for i in range(0, 2):
          c_x[i] = int(input('Digite a coordenada X {}: '.format(i+1)))  
          c_y[i] = int(input('Digite a coordenada Y {}: '.format(i+1)))
  
        res_x = c_x[0] - c_x[1]
        res_y = c_y[0] - c_y[1]

        soma_euclidean = math.sqrt(math.pow(res_x, 2) + math.pow(res_y, 2))

        print('\nO valor da soma Euclidiana e: {}'.format(soma_euclidean))
       
        key = 0

  elif resp == 2:
       
        print('\nQuestão 2 - Determine o ponto máximo da função: \n f(x) = (sen(pi * x) / x ')

        x = np.arange(-5, 5, 0.1)

        # y = np.sin(x)
        y = np.sin(np.pi * x ) / x
        
        # print('{}'.format(y))

        plt.plot(x, y, color="orange", linewidth=2.0)
        plt.title("grafico senoide da funcao Y: ")
        #plt.savefig("teste.png")
        plt.show()

        key = 0

  elif resp == 3:

        print('\nQuestão 3 - Escreva as segintes matrizes: \n 10I[3][3] = {10,0,0,0,10,0,0,0,10}\n I[2][2] = {1,0,0,1}\n')

        matriz1 = [[0, 0], [0, 0]]
        matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


        for n in range(2):
          for o in range(2):
            matriz1[n][o] = int(input(f'digite um valor para matriz 2x2[n, o]: '))
        for l in range(3):
          for m in range(3):
            matriz2[l][m] = int(input(f'digite um valor para matriz 3x3[l, m]: '))

        print('Matriz 2x2: \n')

        for z in range(0, 2):
          print('{}'.format(matriz1[z]))
        print('\nMatriz 3x3: \n')
        for alpha in range(0, 3):
          print('{}'.format(matriz2[alpha]))

        key = 0

  elif resp == 4:

    print('\nQuestão 4 - Execute as seguintes portas logicas: \n a AND b = c \n a OR b = c\n')
    a = input('Digite um valor binario para A: ')
    b = input('Digite um valor binario para B: ')
    
    print('\n')
    
    if (a == '0' or a == '1') and (b == '0' or b == '1'):
      c = a and b
      print('O resultado de {} AND {} = {}'.format(a, b, c))
      c = a or b
      print('O resultado de {} OR {} = {}'.format(a, b, c))
    else: 
      print('Erro quem disse que {}, {} sao binario!!!'.format(a, b))

    key = 0
    
  elif resp == 0:
    key = 1

  else:
      print('\nQuestão não encontrada!')