import random
import os
import copy
import idioma
from collections import Counter

from colorama import Fore, Style, init

# É preciso trocar o endereço da pasta para o que esta no seu computador, até o arquivo nomes.txt
with open(r'C:\Users\bulky\Desktop\Python\Termo\Termo-game-\nomes.txt', 'r', encoding='utf-8') as file:
    palavras = [line.strip().upper() for line in file]


def inicio(voltarmenu):
     idioma_jogo = idioma.get_idioma()  

# É preciso trocar o endereço da pasta para o que esta no seu computador, até o arquivo nomes.txt

     if idioma_jogo == 'Português':
         caminho_arquivo = r'C:\Users\bulky\Desktop\Python\Termo\Termo-game-\nomes.txt'
     else:
         caminho_arquivo = r'C:\Users\bulky\Desktop\Python\Termo\Termo-game-\names.txt'

    # Carrega a lista de palavras do arquivo correto
     with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        palavras = [line.strip().upper() for line in file]
        palavra2 = [line.strip().upper() for line in file]




     letras_usadas = []
     l2 = []
     l1=[]
     venceu = False
     
     os.system("cls")
     palavra = random.choice(palavras).upper()
     palavrav = Fore.LIGHTGREEN_EX + palavra + Style.RESET_ALL
     palavra2 = random.choice(palavras).upper()
     #Descomente para mostrar a resposta no jogo👇
     #print(palavra,palavra2)
     print("_ _ _ _ _  || _ _ _ _ _ ") 
     print()
     Jogo(letras_usadas,l2,l1,venceu,palavra,palavra2,palavrav,voltarmenu)

#Essa função roda o jogo inteiro
def Jogo(letras_usadas,l2,l1,venceu,palavra,palavra2,palavrav,voltarmenu):
     init()
     #Variaveis para controlar o jogo
     controle = 0
     controle2 = 0
     
     l = 5
     c = 6
     p1certa = False
     p2certa = False
     listac = []
     lista2c = []
     # listaincerta = list("11111")
     while c > 0 and not venceu:
          #Essa parte verifica cada tentativa digitada para ter exatamente 5 letras 
          while True:
               if c == 6:
                    tentativa = input("Digite sua tentativa: ").upper()
                    if len(tentativa) == l and tentativa.isalpha():
                         c -= 1
                         break
                    else:
                         print(Fore.RED+"Opção inválida ❌"+Style.RESET_ALL)
                         
               else:
                    tentativa = input("").upper()
                    if len(tentativa) == 5 and tentativa.isalpha():
                         c -= 1
                         break
                    else:
                         print(Fore.RED+"Opção inválida ❌"+Style.RESET_ALL)
                    
     
          lista = []
          lista2 = []
          qtd_letras = Counter(palavra)  # Conta a quantidade  de cada letra da palavra em um dicionario
          qtd_letras2 = Counter(palavra2)  # Conta a quantidade  de cada letra da palavra em um dicionario



          #verifica primeira palavra, com o zip retornando a primeira letra da palavra e da tentativa, e atribuindo respectivamente
          # a letra1 e letra2, e depois comparando e atribuindo as cores
           
          for (letra1, letra2) in zip(palavra,tentativa):

               cont = palavra.count(letra2)
               if letra2 in palavra and letra2 != letra1:
                    #adiciona somente a letra a lista, sem cor, a cor amarela e adicionada no proximo for 
                    lista.append(letra2)
                    letras_usadas.append(Fore.LIGHTMAGENTA_EX+letra2+Style.RESET_ALL)
                    
               elif letra1 == letra2:
                    if qtd_letras[letra2] == 1:
                         #se houver somente uma letra, adiciona a letra a lista com a cor verde, e subtrai menos 1 na qtd_letras daquela letra
                         # na posição dela no dicionario
                         lista.append(Fore.LIGHTGREEN_EX + letra2 + Style.RESET_ALL)
                         qtd_letras[letra2] -= 1
                    if qtd_letras[letra2] == 2:
                         #mesma coisa do de cima 
                         lista.append(Fore.LIGHTGREEN_EX + letra2 + Style.RESET_ALL)
                         qtd_letras[letra2] -= 1
                    letras_usadas.append(Fore.LIGHTMAGENTA_EX+letra2+Style.RESET_ALL)
               else:
                    lista.append(letra2)
                    letras_usadas.append(Fore.LIGHTMAGENTA_EX+letra2+Style.RESET_ALL)

          for i, (letra1, letra2) in enumerate( zip(palavra,tentativa)):
               if letra2 in palavra and letra2 != letra1:
                    if qtd_letras[letra2] == 1:
                         for letra0 in lista:
                              if letra0 == letra2:
                                   lista[i] = (Fore.LIGHTYELLOW_EX + letra2 + Style.RESET_ALL)



          l1 +=  letras_usadas
         
          for letra in l1:
               if letra not in l2:
                    l2.append(letra)


          #verifica segunda palavra
          for  (letra1, letra2) in zip(palavra2,tentativa):
               if letra2 in palavra2 and letra2 != letra1:
                    #adiciona somente a letra a lista, sem cor, a cor amarela e adicionada no proximo for 
                    lista2.append(letra2)
                    letras_usadas.append(Fore.LIGHTMAGENTA_EX+letra2+Style.RESET_ALL)
               elif letra1 == letra2:
                    if qtd_letras2[letra2] == 1:
                         #se houver somente uma letra, adiciona a letra a lista com a cor verde, e subtrai menos 1 na qtd_letras daquela letra
                         # na posição dela no dicionario
                         lista2.append(Fore.LIGHTGREEN_EX + letra2 + Style.RESET_ALL)
                         qtd_letras2[letra2] -= 1

                    if qtd_letras2[letra2] == 2:
                         #mesma coisa do de cima 
                         lista2.append(Fore.LIGHTGREEN_EX + letra2 + Style.RESET_ALL)
                         qtd_letras2[letra2] -= 1
                    letras_usadas.append(Fore.LIGHTMAGENTA_EX+letra2+Style.RESET_ALL)
               else:
                    lista2.append(letra2)
                    letras_usadas.append(Fore.LIGHTMAGENTA_EX+letra2+Style.RESET_ALL)


          for i, (letra1, letra2) in enumerate( zip(palavra2,tentativa)):
               if letra2 in palavra2 and letra2 != letra1:
                    if qtd_letras2[letra2] == 1:
                         for letra0 in lista2:
                              if letra0 == letra2:
                                   lista2[i] = (Fore.LIGHTYELLOW_EX + letra2 + Style.RESET_ALL)

          l1 +=  letras_usadas
 
          for letra in l1:
               if letra not in l2:
                    l2.append(letra)
          
          
          if tentativa == palavra and controle == 0:
               
               p1certa = True
               listac = copy.deepcopy(lista)
               controle += 1
          if tentativa == palavra2 and controle2 == 0 :
               p2certa = True
               lista2c = copy.deepcopy(lista2)
               controle2 += 1



          if p1certa: 
               print(' '.join(listac) + " || " + ' '.join(lista2), f' |   Tentativas:{Fore.LIGHTBLUE_EX+ str(c) +Style.RESET_ALL}   | Letras usadas:',' '.join(l2))
               
          elif p2certa:
               
               print(' '.join(lista) + " || " + ' '.join(lista2c), f' |   Tentativas:{Fore.LIGHTBLUE_EX+str(c)+Style.RESET_ALL}   | Letras usadas:',' '.join(l2))

          elif not p1certa and not p2certa:
                print(' '.join(lista) + " || " + ' '.join(lista2), f' |   Tentativas:{Fore.LIGHTBLUE_EX+str(c)+Style.RESET_ALL}   | Letras usadas:',' '.join(l2))

          

          

          if p1certa and p2certa :
               venceu = True
               print("\n")
               vitoria()
               r = input(' "s" pra jogar novamente "n" para sair ou enter pra voltar ao menu ').upper()
               if c == 0:
                    c +=1
               if r == "S":
                    inicio(voltarmenu)
               elif r == 'N':
                    print("Obrigado por jogar❤️")
               else:
                    print(Fore.LIGHTCYAN_EX+"VOLTANDO PRO MENU "+Style.RESET_ALL+"🤖")
                    input()
                    voltarmenu()


          if c ==0:
               derrota()
               palavra = Fore.LIGHTBLUE_EX+palavra+Style.RESET_ALL
               palavra2 = Fore.LIGHTBLUE_EX+palavra2+Style.RESET_ALL
               if p1certa and not p2certa:
                    print(f"A palavra era {palavra2} burrão🥱")
               elif p2certa and not p1certa:
                    print(f"A palavra era {palavra} burrão🥱")
               else:
                    print(f"As palavras eram {palavra} | {palavra2}  burrão🥱")

               r = input(' "s" pra jogar novamente "n" para sair ou enter pra voltar ao menu ').upper()
               if r == "S":
                    inicio(voltarmenu)
               elif r == 'N':
                    print("Obrigado por jogar❤️")
               else:
                    print(Fore.LIGHTCYAN_EX+"VOLTANDO PRO MENU "+Style.RESET_ALL+"🤖")
                    input()
                    voltarmenu()


def vitoria():
     print(Fore.LIGHTGREEN_EX+"VOCE GANHOU!"+Style.RESET_ALL+"🤪😎")   
        
def derrota():
     print(Fore.RED+"VOOCE PERDEU!"+Style.RESET_ALL+"😂😂")