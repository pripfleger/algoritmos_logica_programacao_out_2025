import os
from colorama import init, Fore

init(autoreset=True)

pecas = {}
caixas = {}
id_peca = 0
numero_caixa = 1

menu =  ("1. Cadastrar nova peça",
         "2. Listar peças aprovadas/reprovadas",
         "3. Remover peça cadastrada",
         "4. Listar caixas",
         "5. Gerar relatório",
         "0. Sair do sistema")

menu_relatorio = ("1. Peças aprovadas",
                  "2. Peças reprovadas",
                  "3. Quantidade total de caixas",
                  "4. Voltar")

def mostrar_menu():
    os.system("cls")
    print (Fore.BLUE + "########## MENU ##########\n")
    for itens in menu:
        print(Fore.BLUE + itens)
    print(Fore.BLUE + "_________________________\n")


def escolha_opcao():
    try:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            cadastrar_peca()
            print (Fore.GREEN + "Peça cadastrada com sucesso!!!")
        elif opcao == 2:
            listar_pecas()
            input("Tecle ENTER para retornar!")
        elif opcao == 3:
            remover_peca()
        elif opcao == 4:
            listar_caixas()
            input("Tecle ENTER para retornar!")
        elif opcao == 5:
            gerar_relatorio()
        elif opcao == 0:
            sair_sistema()
        else:
            print(Fore.RED + "Opção inválida, tente novamente!!!")
            input("Tecle ENTER para retornar!")
    except Exception:
            print(Fore.RED + "Opção não identificada!")

def cadastrar_peca():
    global id_peca
    nome_peca = input(Fore.YELLOW + "Qual o nome da peça? ")
    peso_peca = float(input(Fore.YELLOW + "Qual o peso da peça? "))
    cor_peca = input(Fore.YELLOW + "Qual a cor da peça? ").lower()
    comprimento_peca = float(input(Fore.YELLOW + "Qual o comprimento da peça? "))
    status = classificacao_peca (peso_peca, cor_peca, comprimento_peca)
    pecas[id_peca] = {"Nome":nome_peca,
                      "Peso":peso_peca,
                      "Cor": cor_peca,
                      "Comprimento": comprimento_peca,
                      "Status": status}
    armazenar(id_peca, status)
    id_peca += 1
    input("Tecle ENTER para continuar!")

def classificacao_peca(peso, cor, comprimento):
    if (
        (95<= peso <= 105) and
        (cor == "azul" or cor == "verde") and
        (10 <= comprimento <= 20)
        ):
        status = "Aprovado"
        return status
    else:
        status = "Reprovado"
        return status


def listar_pecas():
    os.system("cls")
    if not pecas:
        print(Fore.RED + "Nenhuma peça cadastrada")
    else:
        print (Fore.YELLOW + "---------- Peças Cadastradas ----------\n")
        for id_peca, item in pecas.items():
            print(Fore.YELLOW + f"--> ID: {id_peca}\n - Nome: {item["Nome"]}\n - Peso: {item["Peso"]}g\n - Cor: {item["Cor"]}\n - Comprimento: {item["Comprimento"]}cm\n - Status: {item["Status"]}\n")


def armazenar(id_peca, status):
    global numero_caixa
    if status == "Aprovado":
        if numero_caixa not in caixas:
            caixas[numero_caixa] = []

        if len(caixas[numero_caixa]) < 10:
            caixas[numero_caixa].append(id_peca)
            print (Fore.GREEN + f"Peça armazenada com sucesso na caixa {numero_caixa}!")
        else:
            numero_caixa += 1
            caixas[numero_caixa] = [id_peca]
            print(Fore.BLUE + f"Caixa anterior fechada!")
            print(Fore.GREEN + f"Peça armazenada com sucesso na caixa {numero_caixa}!")
    else:
        print (Fore.RED + "Peça reprovada, não entra na caixa!!!")


def remover_peca():
    if pecas:
        listar_pecas()
        try:
            peca_excluida = int(input(Fore.YELLOW + "Qual peça deseja excluir? Digite o ID da peça: "))
            if peca_excluida in pecas:
                # Remove das caixas também
                for numero_caixa, items in caixas.items():
                    if peca_excluida in items:
                        items.remove(peca_excluida)
                        print(Fore.GREEN + f"Peça removida da caixa {numero_caixa}")
                        break
                del pecas[peca_excluida]
                print(Fore.GREEN + "Peça removida com sucesso!")
            else:
                print(Fore.RED + "ID não encontrado!")
        except Exception:
            print(Fore.RED + "Erro na exclusão! Tente novamente!")
        input("Tecle ENTER para retornar!")
    else:
        print(Fore.YELLOW + "Não há peça cadastrada! Tente novamente!")
        input("Tecle ENTER para retornar!")


def listar_caixas():
    os.system("cls")
    print(Fore.YELLOW + "---------- Caixas ----------\n")
    if caixas:
        for numero_caixa, items in caixas.items():    
            if len(items) == 10:
                print(Fore.YELLOW + f"Caixa {numero_caixa} FECHADA: itens {items}")
            else:
                print(Fore.YELLOW + f"Caixa {numero_caixa} ABERTA: itens {items}")
    else:
        print(Fore.RED + "Nenhuma caixa criada!")


def gerar_relatorio():
    os.system("cls")
    print (Fore.BLUE + "---------- Relatórios ----------\n")
    for itens in menu_relatorio:
        print(Fore.BLUE + itens)
    print(Fore.BLUE + "_________________________\n")
    try:
        opcao_relatorio = int(input(Fore.YELLOW + "Digite a opção referente ao relatório desejado: "))
        
        if opcao_relatorio == 1:
            pecas_aprovadas = {id_peca: item
                            for id_peca, item in pecas.items()
                            if item["Status"] == "Aprovado"}
            if not pecas_aprovadas:
                print(Fore.RED + "Não foram encontradas peças aprovadas!")
            else:
                os.system("cls")
                print(Fore.YELLOW + "---------- Peças Aprovadas ----------\n")
                for id_peca, item in pecas_aprovadas.items():
                    print(Fore.YELLOW + f"---> Peça {id_peca}\n - Nome: {item["Nome"]}\n - Peso: {item["Peso"]}g\n - Cor: {item["Cor"]}\n - Comprimento: {item["Comprimento"]}cm\n")
            input("Tecle ENTER para retornar!")
            gerar_relatorio()
        
        elif opcao_relatorio == 2:
            pecas_reprovadas = {id_peca: item
                            for id_peca, item in pecas.items()
                            if item["Status"] == "Reprovado"}
            if not pecas_reprovadas:
                print(Fore.RED + "Não foram encontradas peças reprovadas!")
            else:
                os.system("cls")
                print(Fore.YELLOW + "---------- Peças Reprovadas ----------")
                for id_peca, item in pecas_reprovadas.items():
                    print(Fore.YELLOW + f"\n---> Peça {id_peca}\n - Nome: {item["Nome"]}\n - Peso: {item["Peso"]}g\n - Cor: {item["Cor"]}\n - Comprimento: {item["Comprimento"]}cm")
                    if not 95<= item["Peso"] <= 105:
                        print(Fore.RED + " • Peso fora do padrão")
                    if not (item["Cor"] == "azul" or item["Cor"] == "verde"):
                        print(Fore.RED + " • Cor fora do padrão")
                    if not 10 <= item["Comprimento"] <= 20:
                        print(Fore.RED + " • Comprimento fora do padrão")
            input("\nTecle ENTER para retornar!")
            gerar_relatorio()
        
        elif opcao_relatorio == 3:
            os.system("cls")
            print(Fore.YELLOW + f"Total de caixas usadas: {len(caixas)}")
            input("\nTecle ENTER para tentar novamente!")
            gerar_relatorio()
        
        elif opcao_relatorio == 4:
            mostrar_menu()
            escolha_opcao()
        
        else:
            print(Fore.RED + "Opção inválida")
            input("Tecle ENTER para tentar novamente!")
            gerar_relatorio()
    except Exception:
            print(Fore.RED + "Opção não identificada!")

def sair_sistema():
    input(Fore.BLUE + "Saindo do sistema!!!\nTecle ENTER para reiniciar!")

while True:
    os.system("cls")
    mostrar_menu()
    escolha_opcao()