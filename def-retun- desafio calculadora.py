'''Faça um programa de calculadora simples com as seguintes operações
possíveis: adição, subtração, multiplicação e divisão. O programa inicia
apresentando ao usuário um menu de opções como mostrado abaixo:

**********************************************************************
* Calculadora. Opções possíveis:
* 1. Adição
* 2. Subtração
* 3. Multiplicação
* 4. Divisão
* 5. Exponenciação
* 6. Raiz quadrada
* 7. Porcentagem
* 8. Resto da divisão
* 9. Divisão de inteiro
* 0. Sair do programa
*********************************************************************
Informe a opção desejada:


A opção informada é então analisada e o programa executa a operação apropriada,
se a opção for inválida, informe ao usuário e peça a ele para entrar com uma
opção válida.
- Após a execução da operação o programa volta a apresentar o menu inicial até
que o usuário encerre o programa com a opção 0.
- Utilize funções para realizar os cálculos, inclusive para o menu.
- Utilize a estrutura de comparação que melhor se adeque ao problema.
- Mantenha o código fonte organizado.
- Não será aceito utilização de bibliotecas.
'''

def menu():
    print('------------CALCULADORA----------\n')
    print('1. adção')
    print('2. Subtração')
    print('3. multiplicação')
    print('4. divisão')
    print('5. Exponenciação')
    print('6. Raiz quadrada')
    print('7. Porcntagem')
    print('8. Resto da divisão')
    print('9. Divisão de inteiro')
    print('0 Sair do programa\n') 

def soma(num1,num2):
           return num1+num2

def subtracao(num1,num2):
           return num1-num2

def multiplicacao(num1,num2):
           return num1 * num2

def divisao(num1,num2):
           return num1 / num2

def exp (num):
           return num ** 2

def raiz (num):
           return num ** 0.5

def Porcentagem (num, porcentagem):
           return num * porcentagem / 100

def resto_div (num, num2):
           return num % num2 

def divisao_int(num1,num2):
           return num1 // num2

opcao= ''
while opcao != 0:
    menu() #chamando função
    opcao = int(input('digite uma opção:? '))
    
    if opcao == 1:
        print ('-----Adição-------\n')
        num1 = int(input(' informe o 1° numero: '))
        num2 = int(input(' informe o 2° numero: '))
        resultado = soma (num1, num2)
        print (f'soma = {resultado}\n')
           
    elif opcao == 2:
        print   ('-----SUBTRAÇÃO------\n')
        num1 = int(input(' informe o 1° numero: '))
        num2 = int(input(' informe o 2° numero: '))
        resultado = subtracao (num1, num2)
        print (f'subtração = {resultado}\n')

    elif opcao == 3:
        print ('-----MULTIPLICAÇÃO-------\n')
        num1 = int(input(' informe o 1° numero: '))
        num2 = int(input(' informe o 2° numero: '))
        resultado = multiplicacao (num1, num2)
        print (f'multiplicação = {resultado}\n')

    elif opcao == 4:
        print ('-----DIVISÃO-------\n')
        num1 = int(input(' informe o 1° numero: '))
        num2 = int(input(' informe o 2° numero: '))
        resultado = divisao (num1, num2)
        print (f'divisão = {resultado}\n')
    
    elif opcao == 5:
        print ('-----EXPONENCIAÇÃO-------\n')
        num = int(input(' informe um numero: '))
        resultado = exp (num)
        print (f'exponenciação = {resultado}\n')

    elif opcao == 6:
        print ('-----RAIZ QUADRADA-------\n')
        num = int(input(' informe um numero: '))
        resultado = raiz (num)
        print (f'raiz quadrada = {resultado}\n')
    
    elif opcao == 7:
        print ('-----PORCENTAGEM-------\n')
        num = int(input(' informe um numero: '))
        porcentagem = int(input(' informe o valor da porcentagem: '))
        resultado = Porcentagem (num, porcentagem)
        print (f'{porcentagem}% de {num} = {resultado}\n')

    elif opcao == 8:
        print ('-----RESTO DA DIVISÃO-------\n')
        num = int(input(' informe um numero: '))
        num2 = int(input(' informe um numero: '))
        resultado = resto_div (num, num2)
        print (f'o resto da divisão de {num} e {num2} é: {resultado} \n')
    
    elif opcao == 9:
        print ('-----DIVISÃO DE INTEIRO-------\n')
        num1 = int(input(' informe o 1° numero: '))
        num2 = int(input(' informe o 2° numero: '))
        resultado = divisao_int (num1, num2)
        print (f'divisão = {resultado}\n')

    elif opcao == 0:
        print('voce saiu do sistema')
        
    else:
        print('digite uma opção VALIDA')
       



    




    






