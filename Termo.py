import os
import random
from colorama import Fore, Style,init
palavras = [
    "amigo", "campo", "mesmo", "grupo", "vezes", "dever", "velho", "carta", "falta", 
    "baixo", "vindo", "parte", "jeito", "coisa", "valor", "tempo", "livro", "mundo", 
    "porta", "baixo", "nunca", "linha", "verde", "apenas", "outra", "claro", "pouco", 
    "junto", "grande", "banho", "limpo", "prado", "bruto", "carro", "casal", "peixe", 
    "chave", "falso", "longe", "pacto", "roupa", "manso", "velha", "trama", "festa", 
    "muito", "área", "pedra", "árdua", "ritmo", "treta", "corte", "tempo", "ordem", 
    "estar", "pare", "vinho", "vento", "metal", "praia", "trevo", "conto", "prazo", 
    "beira", "crime", "meiga", "sabor", "troca", "tigre", "justa", "sorte", "sonho", 
    "fruta", "curva", "norte", "tarde", "custo", "anexo", "jovem", "pleno", "lugar", 
    "piano", "dente", "troco", "redor", "salvo", "malta", "outro", "canal", "ativo", 
    "laço", "cobra", "barco", "certo", "vinho"]

def mostrar_menu():
    print('''         
   ████████╗███████╗██████╗░███╗░░░███╗░█████╗░
   ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██╔══██╗
   ░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║░░██║
   ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║░░██║
   ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║╚█████╔╝
   ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░    \n\n''' '           Escolha um opção abaixo👇\n\n     1 Palavra |  2 palavras | 4 palavras\n\n')


def inicio():
     venceu = False
     os.system("cls")
     palavra = random.choice(palavras).upper()
     print(palavra)

     print("_ _ _ _ _")
     print()
     print('''Letras:
           
           
           ''')
     Jogo(palavra,venceu)


def Jogo(palavra,venceu):
     init()

     l = 5
     while venceu == False:
          tentativa = input("Digite sua tentativa ")[:l].upper()
          lista = []
          for i, (letra1, letra2) in enumerate(zip(palavra,tentativa)):
               if letra1 == letra2:
                    lista.append(Fore.LIGHTGREEN_EX + letra2 + Style.RESET_ALL)
               else:
                    lista.append(letra2)
          print(' '.join(lista))
          if tentativa == palavra:
               venceu = True
     vitoria()

     
def vitoria():
     print(Fore.LIGHTGREEN_EX+"Voce Ganhou!"+Style.RESET_ALL)   
        



    
    
    

def escolha_opcao():
     opcao_escolhida = int(input("Sua escolha:"))
     if opcao_escolhida == 1:
          inicio()
     elif opcao_escolhida ==2:
          print("Nao ta pronto")
     elif opcao_escolhida == 4:
           print("Nao ta pronto")


def exibir_sub_titulo(texto):
    os.system("cls")
    print(texto)




def main():
       os.system("cls")
       mostrar_menu()
       escolha_opcao()

if __name__ == '__main__':
     main()