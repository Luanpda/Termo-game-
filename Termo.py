import os
import jogo1palavra
import jogo2palavras
from colorama import Fore, Style,init
import idioma

#Arquivo princiapal, execute ele para iniciar o jogo.
termo ='''         
   ████████╗███████╗██████╗░███╗░░░███╗░█████╗░
   ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██╔══██╗
   ░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║░░██║
   ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║░░██║
   ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║╚█████╔╝
   ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░    \n\n'''


    

def mostrar_menu():
    print(Fore.LIGHTCYAN_EX+ termo + Style.RESET_ALL +f'           Escolha um opção abaixo👇\n\n  1 Palavra |  2 palavras | 4 palavras | 5 Regras | 6 Mudar Idioma atual:{idioma.idioma}\n\n')

    


def inicio_jogo(opcao_escolhida): 
     if opcao_escolhida == 1:
          jogo1palavra.inicio(main)
     if opcao_escolhida == 2:
          jogo2palavras.inicio(main)
     
def regras():
     print("REGRAS:\n1-A palvra sempre vai ter 5 letras\n2-Você tem 6 tentativas pra acertar\n3-As letras com a cor "+Fore.GREEN+"verde"+Style.RESET_ALL+" estão corretas, e as letras "+Fore.LIGHTYELLOW_EX+"amarelas"+Style.RESET_ALL+" estão na posição errada")
     input()
     main()



def op_invalida():
     # os.system("cls")
     print(Fore.RED+"SABE ESCREVER NAO ANIMAL"+Style.RESET_ALL+"🤬")
     input()
     main()  
       

def escolha_opcao():
     try:
          opcao_escolhida = int(input("Sua escolha:"))
          if opcao_escolhida == 1:
               inicio_jogo(opcao_escolhida)
          elif opcao_escolhida == 2:
               inicio_jogo(opcao_escolhida)
          elif opcao_escolhida == 4:
               print("Nao ta pronto")
               input()
               main()
          elif opcao_escolhida == 5:
               regras()
          elif opcao_escolhida == 6:
               
               if idioma.idioma == 'Português':
                    idioma.set_idioma('Inglês')
               else:
                    idioma.set_idioma('Português')
               
               
               main()
              
          else:
               op_invalida()
     except Exception as e:
          print(e)


def main():

     os.system("cls")
     mostrar_menu()
     escolha_opcao()
     

if __name__ == '__main__':
     main()