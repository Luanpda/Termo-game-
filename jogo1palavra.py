import random
import os

from colorama import Fore, Style, init

with open(r'C:\Users\bulky\Desktop\Python\Termo\Termo-game-\nomes.txt', 'r', encoding='utf-8') as file:
    palavras = [line.strip().upper() for line in file]


def inicio(voltarmenu):
     letras_usadas = []
     l2 = []
     l1=[]
     venceu = False
     os.system("cls")
     palavra = random.choice(palavras).upper()
     print(palavra)
     print("_ _ _ _ _")
     print()
     Jogo(letras_usadas,l2,l1,venceu,palavra,voltarmenu)


def Jogo(letras_usadas,l2,l1,venceu,palavra,voltarmenu):
     init()
     l = 5
     c = 6
     while c > 0 and venceu == False:
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
          
          
          for i, (letra1, letra2) in enumerate(zip(palavra,tentativa)):
               if letra2 in palavra and letra2 != letra1:
                    lista.append(Fore.LIGHTYELLOW_EX+ letra2 + Style.RESET_ALL)
                    letras_usadas.append(Fore.LIGHTYELLOW_EX+ letra2 + Style.RESET_ALL)
               elif letra1 == letra2:
                    lista.append(Fore.LIGHTGREEN_EX + letra2 + Style.RESET_ALL)
                    letras_usadas.append(Fore.LIGHTGREEN_EX + letra2 + Style.RESET_ALL)
               else:
                    lista.append(letra2)
                    letras_usadas.append(letra2)
          l1 = l1 + letras_usadas
         
          for letra in l1:
               if letra not in l2:
                    l2.append(letra)
          print(' '.join(lista),f' |   Tentativas:{c}   | Letras usadas:',' '.join(l2))
          if tentativa == palavra:
               venceu = True
               vitoria()
               r = input(' "s" pra jogar novamente "n" para sair ou enter pra voltar ao menu ').upper()
               if r == "S":
                    inicio(voltarmenu)
               elif r == 'N':
                    print("Vai se fuder então❤️")
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
                    print("Vai se fuder então❤️")
               else:
                    print(Fore.LIGHTCYAN_EX+"VOLTANDO PRO MENU "+Style.RESET_ALL+"🤖")
                    input()
                    voltarmenu()
def vitoria():
     print(Fore.LIGHTGREEN_EX+"VOCE GANHOU!"+Style.RESET_ALL+"🤪😎")   
        
def derrota():
     print(Fore.RED+"VOOCE PERDEU!"+Style.RESET_ALL+"😂😂")