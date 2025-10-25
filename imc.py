import os
from colorama import init, Fore, Back 
init(autoreset=True)

def limpar_tela_ope():
    os.system('cls' if os.name == "nt" else 'clear')

def pausar():
    input(f"{Fore.YELLOW}Pressione ENTER para continuar...{Fore.RESET}")

def calcular_imc(peso, altura):
    altura_metros = float(altura / 100)
    imc = (peso / (altura_metros * altura_metros))
    imc_arredondado = round(imc, 3)
    return(imc_arredondado)

def imc_faixa(imc):
    if imc <= 18.5:
        faixa = (f"{Fore.YELLOW}baixo peso{Fore.RESET}")
    elif imc <= 24.9:
        faixa = (f"{Fore.GREEN}peso adequado{Fore.RESET}")
    elif imc <= 29.9:
        faixa = (f"{Fore.YELLOW}sobrepeso{Fore.RESET}")
    elif imc <= 34.9:
        faixa = (f"{Fore.YELLOW}obesidade grau I{Fore.RESET}")
    elif imc <= 39.9:
        faixa = (f"{Fore.RED}obesidade grau II{Fore.RESET}")
    else:
        faixa = (f"{Fore.RED}obesidade grau III{Fore.RESET}")
    return(faixa)

def menu_calcular_imc():
    print(f"{Fore.LIGHTBLUE_EX}Preciso saber algumas coisas sobre você para calcular seu IMC.\n")
    peso = int(input(f"{Fore.GREEN}Digite seu peso (somente números) em quilogramas: {Fore.RESET}"))
    altura = int(input(f"{Fore.GREEN}Digite sua altura (somente números) em centímetros: {Fore.RESET}"))
    imc = calcular_imc(peso, altura)
    faixa = imc_faixa(imc)
    print(f"\nSeu IMC é {imc} e você está com {faixa}.\n")
    pausar()
    iniciar_sistema()

def processar_opcao_inicio(opcao):
    if opcao == "1":
        menu_calcular_imc()
    if opcao == "2":
        print(f"{Fore.BLUE}Até mais!")
        exit()

def iniciar_sistema():
    limpar_tela_ope()
    print(f"{Fore.BLUE}{Back.LIGHTCYAN_EX}Olá! Seja bem-vindo!\n")
    print(f"{Fore.BLUE}Temos as seguintes opções para você:")
    print(f"1 - Calcular IMC")
    print(f"2 - Nada. Desejo sair do sistema.")
    opcao = input(f"\n{Fore.GREEN}O que você quer fazer? Digite a opção desejada: {Fore.RESET}")
    limpar_tela_ope()
    processar_opcao_inicio(opcao)

iniciar_sistema()