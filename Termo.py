import os
import random
from colorama import Fore, Style,init

termo ='''         
   ████████╗███████╗██████╗░███╗░░░███╗░█████╗░
   ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██╔══██╗
   ░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║░░██║
   ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║░░██║
   ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║╚█████╔╝
   ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░    \n\n'''

with open(r'Termo-game-\nomes.txt', 'r', encoding='utf-8') as file:
        palavras = [line.strip() for line in file]



def mostrar_menu():
    print(Fore.LIGHTCYAN_EX+ termo + Style.RESET_ALL +'           Escolha um opção abaixo👇\n\n  1 Palavra |  2 palavras | 4 palavras | 5 Regras\n\n')


def inicio():
     letras_usadas = []
     l2 = []
     l1=[]
     venceu = False
     os.system("cls")
     palavra = random.choice(palavras).upper()
     #print(palavra)

     print("_ _ _ _ _")
     print()
     
     Jogo(letras_usadas,l2,l1,venceu,palavra)


def Jogo(letras_usadas,l2,l1,venceu,palavra):
     init()
     l = 5
     c = 6 
     while c > 0 and venceu == False:
     
          if c == 6:
               tentativa = input("Digite sua tentativa: ")[:l].upper()
               c -= 1
          else:
               tentativa = input("")[:l].upper()
               c -= 1
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
               r = input("Quer jogar novamente s/n? ").upper()
               if r == "S":
                    inicio()
               if r == 'N':
                    print("Vai se fuder então❤️")
               else:
                    print(Fore.LIGHTCYAN_EX+"VOLTANDO PRO MENU "+Style.RESET_ALL+"🤖")
                    input()
                    main()
          if c ==0:
               derrota()
               palavra = Fore.MAGENTA+palavra+Style.RESET_ALL
               print(f"A palavra era {palavra} burrão🥱")

               r = input("Quer jogar novamente s/n? ").upper()
               if r == "S":
                    inicio()
               elif r == 'N':
                    print("Vai se fuder então❤️")
               else:
                    print(Fore.LIGHTCYAN_EX+"VOLTANDO PRO MENU "+Style.RESET_ALL+"🤖")
                    input()
                    main()


def regras():
     print("REGRAS:\n1-A palvra sempre vai ter 5 letras\n2-Você tem 6 tentativas pra acertar\n3-As letras com a cor "+Fore.GREEN+"verde"+Style.RESET_ALL+" estão corretas, e as letras "+Fore.LIGHTYELLOW_EX+"amarelas"+Style.RESET_ALL+" estão na posição errada")
     input()
     main()

def vitoria():
     print(Fore.LIGHTGREEN_EX+"VOCE GANHOU!"+Style.RESET_ALL+"🤪😎")   
        
def derrota():
     print(Fore.RED+"VOOCE PERDEU!"+Style.RESET_ALL+"😂😂")

def op_invalida():
     # os.system("cls")
     print(Fore.RED+"SABE ESCREVER NAO ANIMAL"+Style.RESET_ALL+"🤬")
     input()
     main()  
       

def escolha_opcao():
     try:
          opcao_escolhida = int(input("Sua escolha:"))
          if opcao_escolhida == 1:
               inicio()
          elif opcao_escolhida ==2:
               print("Nao ta pronto")
               input()
               main()
          elif opcao_escolhida == 4:
               print("Nao ta pronto")
               input()
               main()
          elif opcao_escolhida == 5:
               regras()
          else:
               op_invalida()
     except:
          op_invalida()


def exibir_sub_titulo(texto):
    os.system("cls")
    print(texto)




def main():
       os.system("cls")
       mostrar_menu()
       escolha_opcao()

if __name__ == '__main__':
     main()