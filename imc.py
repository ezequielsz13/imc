import os
from colorama import init, Fore, Back 
init(autoreset=True)

def limpar_tela_ope():
    os.system('cls' if os.name == "nt" else 'clear')

def calcular_imc(peso, altura):
    altura_metros = float(altura / 100)
    imc = (peso / (altura_metros * altura_metros))
    imc_arredondado = round(imc, 3)
    return(imc_arredondado)

def menu_calcular_imc():
    print(f"{Fore.LIGHTBLUE_EX}Preciso saber algumas coisas sobre você para calcular seu IMC.")
    peso = int(input(f"{Fore.GREEN}Digite seu peso (somente números) em quilogramas: {Fore.RESET}"))
    altura = int(input(f"{Fore.GREEN}Digite sua altura (somente números) em centímetros: {Fore.RESET}"))
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é {imc} e pode seu peso está OOOOOOOO")

def processar_opcao_inicio(opcao):
    if opcao == "1":
        menu_calcular_imc()
    if opcao == "2":
        print(f"{Fore.BLUE}Até mais!")
        exit()

def iniciar_sistema():
    limpar_tela_ope()
    print(f"{Fore.BLUE}{Back.LIGHTCYAN_EX}Olá! Seja bem-vindo!")
    print(f"{Fore.BLUE}Temos as seguintes opções para você:")
    print(f"1 - Calcular IMC")
    print(f"2 - Nada. Desejo sair do sistema.")
    opcao = input(f"{Fore.GREEN}O que você quer fazer? Digite a opção desejada: {Fore.RESET}")
    limpar_tela_ope()
    processar_opcao_inicio(opcao)

iniciar_sistema()