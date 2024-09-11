from time import sleep

def menu():
    try:
        opcao = int(input('''MENU DE OPÇÕES:
    1 - Cadastrar Despesa
    2 - Cadastrar Receita
    3 - Listar Despesas
    4 - Listar Receitas
    5 - Valor Total das Despesas
    6 - Valor Total das Receitas
    7 - Exclusão de Despesa
    8 - Exclusão de Receita
    9 - Sair do Programa

Escolha uma opção: '''))
    except ValueError:
        print(f'O "MENU DE OPÇÕES" só aceita entrada de números inteiros\nTENTE NOVAMENTE!')
    return opcao

def cadastro(arquivo, tipo = str):
    try:
        with open(arquivo, 'a', encoding= 'utf-8') as dados:
            tipo = tipo.capitalize()
            descricao = str(input(f'Descrição da {tipo}: ')).strip().capitalize()
            valor = float(input(f'Valor da {tipo}: '))
            if tipo == "Despesa":
                data = str(input('Quando foi paga: ')).strip()
            else:
                data = str(input('Quando foi recebida: ')).strip()

            dados.write(f"{descricao};{valor};{data};\n")
            print(f'{tipo} cadastrada')
    except ValueError:
        print(f'O Tipo de alguma das variaveis informada está errado\nTENTE NOVAMENTE!')

def listar(arquivo, tipo = str):
    try:
        print(f'Listagem de {tipo.capitalize()}s:')
        with open(arquivo, 'r', encoding= 'utf-8') as dados:
            lista = list(dados.readlines())
            for valor in lista:
                valor = list(valor.split(";"))
                print(f'{valor[0]}\n    Valor: {valor[1]}\n    Data: {valor[2]}\n')
                sleep(0.5)
    except FileNotFoundError:
        print(f'O arquivo informado não existe.\nTENTE NOVAMENTE!')
        open(arquivo,'x')

def total_soma(arquivo, tipo = str):
    try:
        with open(arquivo, 'r', encoding= 'utf-8') as dados:
            soma = 0
            lista = list(dados.readlines())
            for valor in lista:
                valor= list(valor.split(";"))
                soma += float(valor[1])
            print(f'O total das suas {tipo}s é de R$ {soma:.2f}')
    except FileNotFoundError:
        print(f'O arquivo informado não existe.\nTENTE NOVAMENTE!')
        open(arquivo,'x')

def verificar(arquivo, chave = str):
    try:
        with open(arquivo, 'r', encoding= 'utf-8') as dados:
            conteudo = dados.read()
            if conteudo.count(chave) == 0:
                presenca = False
            else:
                presenca = True
        return presenca
    
    except FileNotFoundError:
        print(f'O arquivo informado não existe.\nTENTE NOVAMENTE!')
        open(arquivo,'x')

def excluir(arquivo, tipo = str, chave = str):
    try:
        tipo = tipo.capitalize()
        verificacao = verificar(arquivo, chave)
    
        if verificacao == False:
            print(f'A {tipo} {chave} não está cadastrada. \nTENTE NOVAMENTE!')
        else:
            with open(arquivo, 'r', encoding= 'utf-8') as dados:
                lista = list(dados.readlines())
            with open(arquivo, 'w', encoding= 'utf-8') as dados: 
                repet = []
                for valor in lista:
                    valor = valor.split(";")
                    if chave != valor[0]:
                        dados.write((f"{valor[0]};{valor[1]};{valor[2]};\n"))
                    else:
                        repet.append(valor.copy())
                    
            if len(repet) > 1:
                for cont, repetição in enumerate(repet):
                    print(f'{cont+1}: {repetição[0]}\n    Valor: {repetição[1]}\n    Data: {repetição[2]}\n')
                apagar = int(input(f'Insira o número referente a {tipo} que você quer apagar: '))
                repet.pop(apagar-1)
                with open(arquivo, 'a', encoding= 'utf-8') as dados:
                    for repeticoes in repet:
                        dados.write(f"{repeticoes[0]};{repeticoes[1]};{repeticoes[2]};\n")
            print(f'{tipo} excluida com sucesso')

    except ValueError:
        print(f'O Tipo de alguma das variaveis informada está errado\nTENTE NOVAMENTE!')
    except IndexError:
        print(f'O núremo informado não é valido\nTENTE NOVAMENTE!')

while True:
    try:
        opcao = menu()
    except UnboundLocalError:
        sleep(1)
        continue

    if opcao==1:
        cadastro("base_despesas.txt", "Despesa")
    elif opcao==2:
        cadastro("base_receitas.txt", "receita")
    elif opcao==3:
        listar("base_despesas.txt", "Despesa")
    elif opcao==4:
        listar("base_receitas.txt", "receita")
    elif opcao==5:
        total_soma("base_despesas.txt", "Despesa")
    elif opcao==6:
        total_soma("base_receitas.txt", "receita")
    elif opcao==7:
        chave = str(input(f'Digite o nome da Despesa que deseja excluir: ')).strip().capitalize()
        excluir("base_despesas.txt", "Despesa", chave)
    elif opcao==8:
        chave = str(input(f'Digite o nome da Receita que deseja excluir: ')).strip().capitalize()
        excluir("base_receitas.txt", "receita", chave)
    elif opcao==9:
        print('PROGRAMA FINALISADO')
        break
    else:
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE')
    sleep(1)