import json # Importei a biblioteca json

alunos = {} # criei um dicionário vazio para armazenar os dados dos alunos
turmas = {}

# crie uma função para salvar os dados em um arquivo
def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f: # abre o arquivo no modo de escrita
        json.dump(dados, f) # grava os dados no arquivo usando oJSON

# Função para carregar os dados de um arquivo
def carregar_dados(nome_arquivo):
    try: # roda o codigo abaixo
        with open(nome_arquivo, 'r') as file: # abre o arquivo no modo de leitura
            dicionario = json.load(file) #carrega os dados no arquivo usando oJSON
            return dicionario
    except: # se tiver algum erro no codigo acima quando rodado, executa o bloco a seguir
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

def editar_aluno(): # crie uma funcao para editar os aluno
    print("\nLista de alunos cadastrados:") 
    for matricula, aluno in alunos.items(): # mostra a lista de alunos cadastrados
        print(f"Matrícula: {matricula}")
        print(f"Nome: {aluno['nome']}")
        print(f"Semestre: {aluno['semestre']}")
        print("----------")

    matricula_ou_nome = input("\nDigite a matrícula ou o nome do aluno que você quer editar: ").upper() # recebe a matricula ou o nome, se for o nome poe todo pra maiusculo

    aluno = None
    for matricula, info_aluno in alunos.items():
        if matricula_ou_nome == str(matricula) or matricula_ou_nome.lower() == info_aluno['nome'].lower():
            aluno = info_aluno
            break

    if aluno is None:
        print("Erro: Aluno inexistente.")
        return

    print("\nDados do aluno encontrado:")
    print(f"Matrícula: {aluno['matricula']}")
    print(f"Nome: {aluno['nome']}")
    print(f"Semestre: {aluno['semestre']}")

    novo_nome = input("\nDigite o novo nome do aluno (ou pressione Enter para manter o mesmo): ").upper()
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

def visualizar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\nAlunos cadastrados:\n")
    for matricula, aluno in alunos.items():
        print("Matrícula:", matricula)
        print("Nome:", aluno['nome'])
        print(f"Semestre: {aluno['semestre']}")
        print("----------")

def apagar_aluno():
    print("\nLista de alunos:")
    for matricula, aluno in alunos.items():
        print("\nMatrícula:", matricula)
        print("Nome:", aluno['nome'])
        print(f"Semestre: {aluno['semestre']}")
        print("----------")

    nome_ou_matricula = input("Digite o nome ou a matrícula do aluno a ser apagado: ").upper()

    # Procurar aluno por matrícula
    if nome_ou_matricula in alunos.keys():
        matricula = nome_ou_matricula
        del alunos[matricula]
        salvar_dados(alunos, 'alunos.json')
        print(f"Aluno {nome_ou_matricula} apagado com sucesso!")
        return

    # Procurar aluno por nome
    for matricula, aluno in alunos.items():
        if aluno['nome'].lower() == nome_ou_matricula.lower():
            del alunos[matricula]
            salvar_dados(alunos, 'alunos.json')
            print(f"Aluno {nome_ou_matricula} apagado com sucesso!")
            return
    else:
        print("Aluno não encontrado.")

# parte principal
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