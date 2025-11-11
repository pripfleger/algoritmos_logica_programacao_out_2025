import os
from colorama import init, Fore, Style

init(autoreset=True)

pecas = {}
caixas = {}
id_peca = 0
numero_caixa = 1

menu =  ("1. Cadastrar nova peça",
         "2. Listar peças aprovadas/reprovadas",
         "3. Remover peça cadastrada",
         "4. Listar caixas fechadas",
         "5. Gerar relatório",
         "0. Sair do sistema")

menu_relatorio = ("1. Peças aprovadas",
                  "2. Peças reprovadas",
                  "3. Quantidade total de caixas",
                  "4. Voltar")

def mostrar_menu():
    os.system("cls")
    print ("########## MENU ##########\n")
    for itens in menu:
        print(itens)
    print("_________________________\n")


def escolha_opcao():
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastrar_peca()
        print ("Peça cadastrada com sucesso!!!")
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
        print("Opção inválida, tente novamente!!!")


def cadastrar_peca():
    global id_peca
    nome_peca = input("Qual o nome da peça? ")
    peso_peca = float(input("Qual o peso da peça? "))
    cor_peca = input("Qual a cor da peça? ").lower()
    comprimento_peca = float(input("Qual o comprimento da peça? "))
    status = classificacao_peca (peso_peca, cor_peca, comprimento_peca)
    pecas[id_peca] = {"Nome":nome_peca,
                      "Peso":peso_peca,
                      "Cor": cor_peca,
                      "Comprimento": comprimento_peca,
                      "Status": status}
    armazenar(id_peca, status)
    id_peca += 1


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
    print ("---------- Peças Cadastradas ----------\n")
    for id_peca, item in pecas.items():
        print(f"--> ID: {id_peca}\n - Nome: {item["Nome"]}\n - Peso: {item["Peso"]}g\n - Cor: {item["Cor"]}\n - Comprimento: {item["Comprimento"]}cm\n - Status: {item["Status"]}\n")


def armazenar(id_peca, status):
    global numero_caixa
    if status == "Aprovado":
        if numero_caixa not in caixas:
            caixas[numero_caixa] = []

        if len(caixas[numero_caixa]) < 10:
            caixas[numero_caixa].append(id_peca)
            print (f"Peça armazenada com sucesso na caixa {numero_caixa}!")
        else:
            numero_caixa += 1
            caixas[numero_caixa] = [id_peca]
            print(f"Caixa anterior fechada!")
            print(f"Peça armazenada com sucesso na caixa {numero_caixa}!")
    else:
        print ("Peça reprovada, não entra na caixa!!!")


def remover_peca():
    if pecas:
        listar_pecas()
        try:
            peca_excluida = int(input("Qual peça deseja excluir? Digite o ID da peça: "))
            if peca_excluida in pecas:
                # Remove das caixas também
                for numero_caixa, items in caixas.items():
                    if peca_excluida in items:
                        items.remove(peca_excluida)
                        print(f"Peça removida da caixa {numero_caixa}")
                        break
                del pecas[peca_excluida]
                print("Peça removida com sucesso!")
            else:
                print("ID não encontrado!")
        except Exception:
            print("Erro na exclusão! Tente novamente!")
            input("Tecle ENTER para retornar!")
    else:
        print("Não há peça cadastrada! Tente novamente!")
        input("Tecle ENTER para retornar!")


def listar_caixas():
    os.system("cls")
    print("---------- Caixas ----------\n")
    if caixas:
        for numero_caixa, items in caixas.items():    
            if len(items) == 10:
                print(f"Caixa {numero_caixa} FECHADA: {items}")
            else:
                print(f"A caixa {numero_caixa} não está fechada!")
    else:
        print("Nenhuma caixa criada!")


def gerar_relatorio():
    os.system("cls")
    print ("---------- Relatórios ----------\n")
    for itens in menu_relatorio:
        print(itens)
    print("_________________________\n")
    opcao_relatorio = int(input("Digite a opção referente ao relatório desejado: "))
    
    if opcao_relatorio == 1:
        pecas_aprovadas = {id_peca: item
                           for id_peca, item in pecas.items()
                           if item["Status"] == "Aprovado"}
        if not pecas_aprovadas:
            print("Não foram encontradas peças aprovadas!")
        else:
            os.system("cls")
            print("---------- Peças Aprovadas ----------\n")
            for id_peca, item in pecas_aprovadas.items():
                print(f"---> Peça {id_peca}\n - Nome: {item["Nome"]}\n - Peso: {item["Peso"]}g\n - Cor: {item["Cor"]}\n - Comprimento: {item["Comprimento"]}cm\n")
        input("Tecle ENTER para retornar!")
        gerar_relatorio()
    
    elif opcao_relatorio == 2:
        pecas_reprovadas = {id_peca: item
                           for id_peca, item in pecas.items()
                           if item["Status"] == "Reprovado"}
        if not pecas_reprovadas:
            print("Não foram encontradas peças reprovadas!")
        else:
            os.system("cls")
            print("---------- Peças Reprovadas ----------")
            for id_peca, item in pecas_reprovadas.items():
                print(f"\n---> Peça {id_peca}\n - Nome: {item["Nome"]}\n - Peso: {item["Peso"]}g\n - Cor: {item["Cor"]}\n - Comprimento: {item["Comprimento"]}cm")
                if not 95<= item["Peso"] <= 105:
                    print(" • Peso fora do padrão")
                if not (item["Cor"] == "azul" or item["Cor"] == "verde"):
                    print(" • Cor fora do padrão")
                if not 10 <= item["Comprimento"] <= 20:
                    print(" • Comprimento fora do padrão")
        input("\nTecle ENTER para retornar!")
        gerar_relatorio()
    
    elif opcao_relatorio == 3:
        os.system("cls")
        print(f"Total de caixas usadas: {len(caixas)}")
        input("\nTecle ENTER para tentar novamente!")
        gerar_relatorio()
    
    elif opcao_relatorio == 4:
        mostrar_menu()
        escolha_opcao()
    
    else:
        print("Opção inválida")
        input("Tecle ENTER para tentar novamente!")
        gerar_relatorio()
    
#-Total de peças aprovadas
#-Total de peças reprovadas e o motivo da reprovação
#-Quantidade de caixas utilizadas

def sair_sistema():
    input("Saindo do sistema!!!\nTecle ENTER para reiniciar!")

while True:
    os.system("cls")
    mostrar_menu()
    escolha_opcao()