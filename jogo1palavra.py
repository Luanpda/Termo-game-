import random
import os


from colorama import Fore, Style, init

# É preciso trocar o endereço da pasta para o que esta no seu computador, até o arquivo nomes.txt
with open(r'C:\Users\bulky\Desktop\Python\Termo\Termo-game-\nomes.txt', 'r', encoding='utf-8') as file:
    palavras = [line.strip().upper() for line in file]


def inicio(voltarmenu):
     letras_usadas = []
     l2 = []
     l1=[]
     venceu = False
     os.system("cls")
     palavra = random.choice(palavras).upper()
     #Descomente para mostrar a resposta no jogo👇
     # print(palavra)
     print("_ _ _ _ _")
     print()
     Jogo(letras_usadas,l2,l1,venceu,palavra,voltarmenu)

#Essa função roda o jogo inteiro
def Jogo(letras_usadas,l2,l1,venceu,palavra,voltarmenu):
     init()
     #Variaveis para controlar o jogo
     l = 5
     c = 6
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
                    if len(tentativa) == l and tentativa.isalpha():
                         c -= 1
                         break
                    else:
                         print(Fore.RED+"Opção inválida ❌"+Style.RESET_ALL)
                    

          lista = []
          
          #verifica primeira palavra, com o zip retornando a primeira letra da palavra e da tentativa, e atribuindo respectivamente
          # a letra1 e letra2, e depois comparando e atribuindo as cores
          for  (letra1, letra2) in zip(palavra,tentativa):
               if letra2 in palavra and letra2 != letra1:
                    lista.append(Fore.LIGHTYELLOW_EX+ letra2 + Style.RESET_ALL)
                    letras_usadas.append(Fore.LIGHTMAGENTA_EX+letra2+Style.RESET_ALL)
               elif letra1 == letra2:
                    lista.append(Fore.LIGHTGREEN_EX + letra2 + Style.RESET_ALL)
                    letras_usadas.append(Fore.LIGHTMAGENTA_EX+letra2+Style.RESET_ALL)
               else:
                    lista.append(letra2)
                    letras_usadas.append(Fore.LIGHTMAGENTA_EX+letra2+Style.RESET_ALL)
          l1 = l1 + letras_usadas
         
          for letra in l1:
               if letra not in l2:
                    l2.append(letra)


          print(' '.join(lista),f' |   Tentativas:{Fore.LIGHTBLUE_EX+ str(c) +Style.RESET_ALL}   | Letras usadas:',' '.join(l2))

          
          if tentativa == palavra:
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
               palavra = Fore.MAGENTA+palavra+Style.RESET_ALL

               print(f"A palavra era {palavra} burrão🥱")

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