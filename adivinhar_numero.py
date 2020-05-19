import os
import platform

def limpar():
    if platform.system == 'Windows': 
        os.system('cls')
    else:
        os.system('clear')

def jogar():   

    print('*****Jogo Adivinhe um Numero*****')
    print('')

    numero = int(input('Numero a ser adivinhado: '))
    
    limpar()  

    while(1):           

        opcao = int(input('Chute: '))
        
        if(opcao > numero):
            print('Numero é menor')
        
        elif(opcao < numero):
            print('Numero é maior')
        
        elif( opcao == numero):
            print(f'Acertou Mizzeeráviii !! O numero era {numero} mesmo !' )
            op = str(input('Deseja Jogar novamente ? (Sim)/(Não) '))
            print('')
            if(op == 'Sim' or op == 'sim' or op == 's' or op == 'S'):                
                jogar()
            else:
                break

jogar()
