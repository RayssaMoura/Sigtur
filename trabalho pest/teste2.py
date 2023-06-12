import json

turmas = {}
professores = {}
alunos = {}

# Função para salvar os dados em um arquivo
def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f)
 
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            dicionario = json.load(file)
            return dicionario
    except FileNotFoundError:
        return {}

# Carregar dados existentes (se houver)
turmas = carregar_dados('turmas.json')
professores = carregar_dados('professores.json')
alunos = carregar_dados('alunos.json')

# Sistema de gestão de turmas

def criar_turma():
    nome_turma = input("Digite o nome da disciplina: ")
    professor = escolher_professor()
    alunos_turma = escolher_alunos()
    
    turma = {
        'nome': nome_turma,
        'professor': professor,
        'alunos': alunos_turma
    }
    
    # Salvar turma no sistema
    turmas[nome_turma] = turma
    salvar_dados(turmas, 'turmas.json')
    
    print("Turma criada com sucesso!")

def editar_turma():
    nome_turma = input("Digite o nome da disciplina da turma a ser editada: ")
    
    if nome_turma in turmas:
        turma = turmas[nome_turma]
        professor = escolher_professor()
        
        opcao = input("Deseja adicionar ou remover um aluno? (adicionar/remover): ")
        if opcao.lower() == 'adicionar':
            alunos_turma = escolher_alunos()
            turma['alunos'] += alunos_turma
        elif opcao.lower() == 'remover':
            aluno_remover = escolher_aluno(turma['alunos'])
            turma['alunos'].remove(aluno_remover)
        
        turma['professor'] = professor
        
        # Atualizar turma no sistema
        turmas[nome_turma] = turma
        salvar_dados(turmas, 'turmas.json')
        
        print("Turma atualizada com sucesso!")
    else:
        print("Turma não encontrada.")

def escolher_alunos(alunos):
    while True:
        print("\n===== ALUNOS =====")
        for aluno in alunos:
            print(f"{aluno['matricula']}. {aluno['nome']}")
        
        escolha = input("Digite o nome ou número da matrícula do aluno: ")
        
        for aluno in alunos:
            if aluno['nome'].lower() == escolha.lower() or aluno['matricula'] == escolha:
                return aluno
        
        print("Aluno não encontrado. Tente novamente.")

def ver_turma():
    nome_turma = input("Digite o nome da disciplina da turma a ser visualizada: ")
    
    if nome_turma in turmas:
        turma = turmas[nome_turma]
        print("Turma:", turma['nome'])
        print("Professor:", turma['professor']['nome'])
        print("Alunos:")
        for aluno in turma['alunos']:
            print(aluno['nome'])
    else:
        print("Turma não encontrada.")

def apagar_turma():
    nome_turma = input("Digite o nome da disciplina da turma a ser apagada: ")
    
    if nome_turma in turmas:
        # Apagar turma do sistema
        del turmas[nome_turma]
        salvar_dados(turmas, 'turmas.json')
        
        print("Turma apagada com sucesso!")
    else:
        print("Turma não encontrada.")

def cadastrar_professor():
    nome_professor = input("Digite o nome do professor: ")
    matricula = len(professores) + 1
    
    professor = {
        'nome': nome_professor,
        'matricula': matricula
    }
    
    # Salvar professor no sistema
    professores[matricula] = professor
    salvar_dados(professores, 'professores.json')
    
    print("Professor cadastrado com sucesso!")

def editar_professor():
    matricula = int(input("Digite a matrícula do professor a ser editado: "))
    
    if matricula in professores:
        professor = professores[matricula]
        nome_professor = input("Digite o novo nome do professor: ")
        
        professor['nome'] = nome_professor
        
        # Atualizar professor no sistema
        professores[matricula] = professor
        salvar_dados(professores, 'professores.json')
        
        print("Professor atualizado com sucesso!")
    else:
        print("Professor não encontrado.")

def ver_dados_professor():
    matricula = int(input("Digite a matrícula do professor a ser visualizado: "))
    
    if matricula in professores:
        professor = professores[matricula]
        print("Matrícula:", professor['matricula'])
        print("Nome:", professor['nome'])
    else:
        print("Professor não encontrado.")

def excluir_professor():
    matricula = int(input("Digite a matrícula do professor a ser excluído: "))
    
    if matricula in professores:
        # Verificar se o professor está vinculado a alguma turma
        turmas_professor = [turma_nome for turma_nome, turma in turmas.items() if turma['professor']['matricula'] == matricula]
        
        if len(turmas_professor) > 0:
            print("O professor está vinculado às seguintes turmas:")
            for turma_nome in turmas_professor:
                print(turma_nome)
            
            opcao = input("Deseja remover o professor mesmo assim? (s/n): ")
            if opcao.lower() != 's':
                return
        
        # Apagar professor do sistema
        del professores[matricula]
        salvar_dados(professores, 'professores.json')
        
        print("Professor excluído com sucesso!")
    else:
        print("Professor não encontrado.")

def visualizar_turmas_professor():
    matricula = int(input("Digite a matrícula do professor: "))
    
    turmas_professor = [turma_nome for turma_nome, turma in turmas.items() if turma['professor']['matricula'] == matricula]
    
    if len(turmas_professor) > 0:
        print("Turmas vinculadas ao professor:")
        for turma_nome in turmas_professor:
            print(turma_nome)
    else:
        print("Nenhuma turma encontrada para o professor.")

def visualizar_alunos_turma():
    nome_turma = input("Digite o nome da disciplina da turma: ")
    
    if nome_turma in turmas:
        turma = turmas[nome_turma]
        print("Alunos da turma:")
        for aluno in turma['alunos']:
            print(aluno['nome'])
    else:
        print("Turma não encontrada.")

def cadastrar_aluno():
    nome_aluno = input("Digite o nome do aluno: ")
    matricula = len(alunos) + 1
    
    aluno = {
        'nome': nome_aluno,
        'matricula': matricula
    }
    
    # Salvar aluno no sistema
    alunos[matricula] = aluno
    salvar_dados(alunos, 'alunos.json')
    
    print("Aluno cadastrado com sucesso!")

def editar_aluno():
    matricula = int(input("Digite a matrícula do aluno a ser editado: "))
    
    if matricula in alunos:
        aluno = alunos[matricula]
        nome_aluno = input("Digite o novo nome do aluno: ")
        
        aluno['nome'] = nome_aluno
        
        # Atualizar aluno no sistema
        alunos[matricula] = aluno
        salvar_dados(alunos, 'alunos.json')
        
        print("Aluno atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")

def visualizar_alunos():
    print("Alunos cadastrados:")
    for matricula, aluno in alunos.items():
        print("Matrícula:", matricula)
        print("Nome:", aluno['nome'])
        print()

def apagar_aluno():
    matricula = int(input("Digite a matrícula do aluno a ser apagado: "))
    
    if matricula in alunos:
        # Verificar se o aluno está vinculado a alguma turma
        turmas_aluno = [turma_nome for turma_nome, turma in turmas.items() if any(aluno['matricula'] == matricula for aluno in turma['alunos'])]
        
        if len(turmas_aluno) > 0:
            print("O aluno está vinculado às seguintes turmas:")
            for turma_nome in turmas_aluno:
                print(turma_nome)
            
            opcao = input("Deseja remover o aluno mesmo assim? (s/n): ")
            if opcao.lower() != 's':
                return
        
        # Apagar aluno do sistema
        del alunos[matricula]
        salvar_dados(alunos, 'alunos.json')
        
        print("Aluno apagado com sucesso!")
    else:
        print("Aluno não encontrado.")

# Função auxiliar para escolher um professor da lista
def escolher_professor():
    print("Professores cadastrados:")
    for matricula, professor in professores.items():
        print("Matrícula:", matricula)
        print("Nome:", professor['nome'])
        print()
    
    while True:
        matricula = int(input("Digite a matrícula do professor desejado: "))
        
        if matricula in professores:
            return professores[matricula]
        else:
            print("Professor não encontrado. Tente novamente.")

# Função auxiliar para escolher um aluno da lista
def escolher_aluno(alunos_disponiveis):
    print("Alunos disponíveis:")
    for aluno in alunos_disponiveis:
        print("Matrícula:", aluno['matricula'])
        print("Nome:", aluno['nome'])
        print()
    
    while True:
        matricula = int(input("Digite a matrícula do aluno desejado: "))
        
        if any(aluno['matricula'] == matricula for aluno in alunos_disponiveis):
            return next(aluno for aluno in alunos_disponiveis if aluno['matricula'] == matricula)
        else:
            print("Aluno não encontrado. Tente novamente.")

def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Coordenador")
        print("2. Professor")
        print("3. Aluno")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            menu_coordenador()
        elif opcao == '2':
            menu_professor()
        elif opcao == '3':
            menu_aluno()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_coordenador():
    while True:
        print("\n===== MENU COORDENADOR =====")
        print("1. Criar turma")
        print("2. Editar turma")
        print("3. Ver turma")
        print("4. Apagar turma")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            criar_turma()
        elif opcao == '2':
            editar_turma()
        elif opcao == '3':
            ver_turma()
        elif opcao == '4':
            apagar_turma()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_professor():
    while True:
        print("\n===== MENU PROFESSOR =====")
        print("1. Cadastrar novo professor")
        print("2. Editar professor cadastrado")
        print("3. Ver dados de um professor cadastrado")
        print("4. Excluir um professor cadastrado")
        print("5. Visualizar turmas de um professor específico")
        print("6. Visualizar os alunos da turma de um professor específico")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_professor()
        elif opcao == '2':
            editar_professor()
        elif opcao == '3':
            ver_dados_professor()
        elif opcao == '4':
            excluir_professor()
        elif opcao == '5':
            visualizar_turmas_professor()
        elif opcao == '6':
            visualizar_alunos_turma()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_aluno():
    while True:
        print("\n===== MENU ALUNO =====")
        print("1. Cadastrar novo aluno")
        print("2. Editar aluno cadastrado")
        print("3. Visualizar alunos cadastrados")
        print("4. Apagar aluno cadastrado")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
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

# Executar o programa
menu_principal()
