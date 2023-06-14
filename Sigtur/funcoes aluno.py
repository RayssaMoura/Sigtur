import json # Importei a biblioteca json

alunos = {} # criei um dicionário vazio para armazenar os dados dos alunos


# criei uma função para salvar os dados em um arquivo
def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f: # abre o arquivo no modo de escrita
        json.dump(dados, f) # grava os dados no arquivo usando o JSON

# Função para carregar os dados de um arquivo
def carregar_dados(nome_arquivo):
    try: # roda o codigo abaixo
        with open(nome_arquivo, 'r') as file: # abre o arquivo no modo de leitura
            dicionario = json.load(file) #carrega os dados no arquivo usando oJSON
            return dicionario
    except ArquivoNaoEncontradoError:  # se tiver algum erro no codigo acima quando rodado, executa o bloco a seguir
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
    for matricula, aluno in alunos.items(): # mostra a lista de alunos cadastrados
        print(f"Matrícula: {matricula}")
        print(f"Nome: {aluno['nome']}")
        print(f"Semestre: {aluno['semestre']}")
        print("----------")


    nome_ou_matricula = input("\nDeseja editar por matrícula (M) ou por nome (N)? ").upper()
    
    if nome_ou_matricula == "M":
        matricula = input("\nDigite a matrícula do aluno a ser editado: ")
        print("\nDados do aluno encontrado:")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Semestre: {aluno['semestre']}")

        if matricula in alunos:
            aluno = alunos[matricula]
            novo_nome = input("\nDigite o novo nome do aluno (ou pressione Enter para manter o mesmo): ").upper()
            novo_semestre = input("Digite o novo semestre do aluno (ou pressione Enter para manter o mesmo): ")
            
            if novo_nome: # verifica se foi digitado um novo nome
                aluno['nome'] = novo_nome # se tiver sido, atualiza o nome do aluno com o novo nome digitado
            if novo_semestre:  # verifica se foi digitado um novo semestre
                aluno['semestre'] = novo_semestre  # se tiver sido, atualiza o semestre do aluno com o novo digitado

            if not novo_nome and not novo_semestre: # verifica se nenhum novo nome e novo semestre foram digitados. 
                print("Nenhum dado foi alterado.") # se nao, mostra que nada foi alterado
            else: # se pelo menos algum tiver sido mudado,
                salvar_dados(alunos, 'alunos.json') # salva os dados atualizados no arquivo alunos. json
                print("Aluno editado com sucesso.") 

    elif nome_ou_matricula == "N":
        novo_nome = input("Digite o nome do aluno a ser editado: ").upper()
        
        for matricula, aluno in alunos.items():
            if aluno['nome'] == novo_nome:
                novo_nome = input("Digite o novo nome do aluno (ou pressione Enter para manter o mesmo): ")
                novo_semestre = input("Digite o novo semestre do aluno (ou pressione Enter para manter o mesmo): ")
                
                if novo_nome: # verifica se foi digitado um novo nome
                    aluno['nome'] = novo_nome # se tiver sido, atualiza o nome do aluno com o novo nome digitado
                if novo_semestre:  # verifica se foi digitado um novo semestre
                    aluno['semestre'] = novo_semestre  # se tiver sido, atualiza o semestre do aluno com o novo digitado

                if not novo_nome and not novo_semestre: # verifica se nenhum novo nome e novo semestre foram digitados. 
                    print("Nenhum dado foi alterado.") # se nao, mostra que nada foi alterado
                else: # se pelo menos algum tiver sido mudado,
                    salvar_dados(alunos, 'alunos.json') # salva os dados atualizados no arquivo alunos. json
                    print("Aluno editado com sucesso.") 
        
            else:
                print("Professor não encontrado.")
            
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

def apagar_aluno(): # crie uma funcao para apagar alunos
    print("\nLista de alunos:") # mostra a lista de alunos
    for matricula, aluno in alunos.items():
        print("\nMatrícula:", matricula)
        print("Nome:", aluno['nome'])
        print(f"Semestre: {aluno['semestre']}")
        print("----------")

    nome_ou_matricula = input("Digite o nome ou a matrícula do aluno a ser apagado: ").upper() #recebe o nome ou a matricula e transforma pra maiusculo

    # Procura o aluno pela matrícula
    if nome_ou_matricula in alunos.keys(): #verifica se a matricula tá como uma das chaves (matriculas) no dic 
        matricula = nome_ou_matricula # se tiver, recebe a matricula
        del alunos[matricula] # e remove o aluno correspondente a matricula do dic alunos
        salvar_dados(alunos, 'alunos.json') #salva os dados atualizados no arquivo alunos. json
        print(f"Aluno {nome_ou_matricula} apagado com sucesso!")
        return

    # Procura o aluno pelo nome
    for matricula, aluno in alunos.items(): # percorre o dic alunos
        if aluno['nome'].lower() == nome_ou_matricula.lower(): # verifica se o nome e igual ao digitado
            del alunos[matricula] # remove o aluno correspondente a matricula do dic alunos
            salvar_dados(alunos, 'alunos.json') #salva os dados atualizados no arquivo alunos. json
            print(f"Aluno {nome_ou_matricula} apagado com sucesso!")
            return
    else:
        print("Aluno não encontrado.")

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