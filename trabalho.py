key = 0
print('Trabalho Computacional\nEmanuel Ávila Cruz Pires\nmatricula: 540286\n\n')
while key == 0:
    print('Escolha uma questão:\n\n 0 - sair')
    resp = input('-> ')
    resp = int(resp)
    if resp == 1:
        print('Questão 1 - Calcular medida Euclidiana entre dois pontos em um plano: \n')
        # recebe os valores que servirão de coordenada
        c_x = input('Digite a coordenada X: ')
        c_y = input('Digite a coordenada Y: ')

        key = 0
    elif resp == 2:
        print('Questão 2 - Determine o ponto máximo da função: \n f(x) = (sen(pi * x) / x ')
        key = 0
    elif resp == 3:
        print('Questão 3 - Escreva as segintes matrizes: \n I[2][2] = {1,0,0,1}\n 10I[3][3] = {10,0,0,0,10,0,0,0,10}')
        key = 0
    elif resp == 4:
        print('Questão 4 - Execute as seguintes portas lògicas: \n C = A && B\n C = A || B')
        key = 0
    elif resp == 0:
        key = 1
    else:
        print('Questão não encontrada!')