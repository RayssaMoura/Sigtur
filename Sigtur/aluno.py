import json # Importei a biblioteca json

alunos = {} # criei um dicionário vazio para armazenar os dados dos alunos


# criei uma função para salvar os dados em um arquivo
def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f: # abre o arquivo no modo de escrita
        json.dump(dados, f) # grava os dados no arquivo usando o JSON

# Função para carregar os dados de um arquivo
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            dicionario = json.load(file)
            return dicionario
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não está no formato JSON válido.")
        return {}


# Carregar dados existentes (se houver) 
alunos = carregar_dados('alunos.json')
turmas = carregar_dados('turmas.json')

# Funções Menu Aluno

def cadastrar_aluno(): #define a funcao de cadastro de alunos
    while True:
        nome_aluno = input("- Digite o nome do Aluno: ").upper() # recebe o nome do aluno e deixa todo maiusculo

        if not nome_aluno.replace(" ", "").isalpha(): #verifica se o nome tem apenas caracteres alfabeticos, removendo todos os espacos em branco com o replace e dps usa o isalpha p verificar se tem apenas letras
            print("Erro: O nome deve conter apenas letras e espaços.") # se tiver numeros, aparece essa mensagem
        elif len(nome_aluno.split()) < 2: #verifica se o nome tem menos de duas palavras, usando o split dividir em palavras e dps verifica se a quantidade de palavras è menor que 2
            print("Erro: O nome deve ser composto por nome e sobrenome.") # se for, retorna a msg de erro
        elif aluno_existente(nome_aluno): # verifica se um aluno com o nome digitado ja existe
            print("Erro: Já existe um aluno cadastrado com o mesmo nome.") # se existir aparece a msg de erro
        else:
            break # se nao para

    while True:
        semestre_aluno = input("- Digite o semestre do Aluno: ") # recebe o numero da matricula

        if not semestre_aluno.isdigit(): # verifica se foi digitado apenas numero
            print("Erro: O semestre deve ser um valor numérico.") # se nao tiver sido, mostra a msg de erro
        else:
            break # se tiver sido digitado apenas numeros, para
    
    matricula = gerar_matricula(alunos) # recebe alunos como argumento e gera uma nova matricula
    dados = { # cria  o dicionario que vai ter as informacoes do aluno 
        'nome': nome_aluno,
        'matricula': matricula,
        'semestre': semestre_aluno,
        'turmas': []
    }
    alunos[matricula] = dados #adiciona as info do aluno ao dic alunos, usando a matricula como indetificacao
    salvar_dados(alunos, 'alunos.json') #salva essas informações no arquivo alunos.json
    print(f"Aluno(a) {nome_aluno} de matrícula número {matricula} do {semestre_aluno} semestre cadastrado com sucesso!")

def aluno_existente(nome):  # crie uma funcao pra verificar se existe algum aluno com o mesmo nome no dic alunos
    for aluno in alunos.values(): # percorre cada aluno no dic alunos.
        if aluno['nome'] == nome: #  verifica se o nome do aluno e igual ao nome digitado.
            return True
    return False

def gerar_matricula(alunos):
    matricula = len(alunos) + 1 # ver o total de alunos e incrementa mais um
    return matricula 

def editar_aluno():
    if not alunos:
        print("Não há alunos cadastrados.")
        return

    print("\nLista de alunos cadastrados:")
    for matricula, aluno in alunos.items():
        print(f"Matrícula: {matricula}")
        print(f"Nome: {aluno['nome']}")
        print(f"Semestre: {aluno['semestre']}")
        print("----------")

    nome_ou_matricula = input("\nDeseja editar por matrícula (M) ou por nome (N)? ").upper()

    if nome_ou_matricula == "M":
        while True:
            matricula = input("\nDigite a matrícula do aluno a ser editado: ")

            if matricula.isdigit():
                if matricula in alunos:
                    aluno = alunos[matricula]
                    print("\nDados do aluno encontrado:")
                    print(f"Matrícula: {matricula}")
                    print(f"Nome: {aluno['nome']}")
                    print(f"Semestre: {aluno['semestre']}")

                    novo_nome = input("\nDigite o novo nome do aluno (ou pressione Enter para manter o mesmo): ")
                    novo_semestre = input("Digite o novo semestre do aluno (ou pressione Enter para manter o mesmo): ")

                    if novo_nome:
                        aluno['nome'] = novo_nome
                    if novo_semestre:
                        aluno['semestre'] = novo_semestre

                    if not novo_nome and not novo_semestre:
                        print("Nenhum dado foi alterado.")
                    else:
                        salvar_dados(alunos, 'alunos.json')
                        print("Aluno editado com sucesso.")
                    break
                else:
                    print("Aluno não encontrado.")
            else:
                print("A matrícula é composta apenas por números. Digite novamente.")

    elif nome_ou_matricula == "N":
        while True:
            novo_nome = input("Digite o nome do aluno a ser editado: ").upper()

            if novo_nome.replace(" ", "").isalpha():
                aluno_encontrado = False

                for matricula, aluno in alunos.items():
                    if aluno['nome'].upper() == novo_nome:
                        aluno_encontrado = True
                        print("\nDados do aluno encontrado:")
                        print(f"Matrícula: {matricula}")
                        print(f"Nome: {aluno['nome']}")
                        print(f"Semestre: {aluno['semestre']}")

                        novo_nome = input("\nDigite o novo nome do aluno (ou pressione Enter para manter o mesmo): ")
                        novo_semestre = input("Digite o novo semestre do aluno (ou pressione Enter para manter o mesmo): ")

                        if novo_nome:
                            aluno['nome'] = novo_nome
                        if novo_semestre:
                            aluno['semestre'] = novo_semestre

                        if not novo_nome and not novo_semestre:
                            print("Nenhum dado foi alterado.")
                        else:
                            salvar_dados(alunos, 'alunos.json')
                            print("Aluno editado com sucesso.")
                        break

                if not aluno_encontrado:
                    print("Aluno não encontrado.")
                break
            else:
                print("O nome deve conter apenas letras e espaços. Digite novamente.")

    else:
        print("Opção inválida. Tente novamente.")

def visualizar_alunos(): # crie uma funcao para vizualizar os alunos cadastrados
    if not alunos: # se nao tiver nenhum aluno cadastrado,
        print("Nenhum aluno cadastrado.") # mostra a mensagem
        return

    print("\nAlunos cadastrados:\n") # se tiver, mostra a lista de aluinos, com as informacoes sobre eles 
    for matricula, aluno in alunos.items():
        print("Matrícula:", matricula)
        print("Nome:", aluno['nome'])
        print(f"Semestre: {aluno['semestre']}")
        print("----------")

def apagar_aluno():
    if not alunos:
        print("Não há alunos cadastrados.")
        return
    
    print("\nLista de alunos:")
    for matricula, aluno in alunos.items():
        print("\nMatrícula:", matricula)
        print("Nome:", aluno['nome'])
        print(f"Semestre: {aluno['semestre']}")
        print("----------")

    nome_ou_matricula = input("\nDeseja apagar por matrícula (M) ou por nome (N)? ").upper()

    if nome_ou_matricula == 'M':
        while True:
            matricula = input("Digite a matrícula do aluno a ser apagado: ")
            if matricula.isdigit():
                if matricula in alunos:
                    del alunos[matricula]
                    salvar_dados(alunos, 'alunos.json')
                    print(f"Aluno com matrícula {matricula} apagado com sucesso!")
                    break
                else:
                    print("Aluno não encontrado.")
            else:
                print("A matrícula deve conter apenas números. Digite novamente.")

    elif nome_ou_matricula == 'N':
        while True:
            nome = input("Digite o nome do aluno a ser apagado: ").upper()
            if nome.replace(" ", "").isalpha():
                encontrou_aluno = False
                for matricula, aluno in alunos.items():
                    if aluno['nome'].upper() == nome:
                        del alunos[matricula]
                        salvar_dados(alunos, 'alunos.json')
                        print(f"Aluno com nome {nome} apagado com sucesso!")
                        encontrou_aluno = True
                        break

                if not encontrou_aluno:
                    print("Aluno não encontrado.")
                break
            else:
                print("O nome deve conter apenas letras e espaços. Digite novamente.")

    else:
        print("Opção inválida.")

# Programa principal
while True:
    print("\n+=================================================Bem-vindo ao Menu Aluno!============================================================+")
    print("|......................Aqui você terá acesso a todas as opções para gerenciar as informações do aluno.................................|")
    print("\n|--MENU ALUNO ------------------------------------------------------------------------------------------------------------------------|")
    print("| (1) - Cadastrar novo aluno: Adicione um novo aluno ao sistema, fornecendo informações como nome e semestre                          |")
    print("| (2) - Editar aluno cadastrado: Faça alterações nos dados de um aluno já cadastrado, como nome e semestre                            |")
    print("| (3) - Visualizar alunos cadastrados: Veja a lista completa de alunos cadastrados no sistema, com seus respectivos detalhes.         |")
    print("| (4) - Apagar aluno cadastrado: Remova um aluno do sistema, excluindo todas as informações relacionadas a ele.                       |")
    print("| (0) - Voltar para o menu principal: Retorne ao menu principal para acessar outras funcionalidades do SiGTur.                        |")
    print("--------------------------------------------------------------------------------------------------------------------------------------+")
    opcao = input(">>> Escolha uma das opções acima: ")

    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        editar_aluno()
    elif opcao == '3':
        visualizar_alunos()
    elif opcao == '4':
        apagar_aluno()
    elif opcao == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")