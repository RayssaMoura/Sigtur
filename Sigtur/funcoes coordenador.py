import json

turmas = {}
professores = {}
alunos = {}

def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f: 
        json.dump(dados, f) 


def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file: 
            dicionario = json.load(file)
            return dicionario
    except:
        return {}

def criar_turma():
    nome_turma = input("Digite o nome da disciplina: ")
    professor_turma = escolher_professor()
    alunos_turma = escolher_alunos()
    
    turma = {
        'nome': nome_turma,
        'professor': professor_turma,
        'alunos': alunos_turma
    }
    
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
            aluno_remover = escolher_alunos(turma['alunos'])
            turma['alunos'].remove(aluno_remover)
        
        turma['professor'] = professor
        
        
        turmas[nome_turma] = turma
        salvar_dados(turmas, 'turmas.json')
        
        print("Turma atualizada com sucesso!")
    else:
        print("Turma não encontrada.")

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
        del turmas[nome_turma]
        salvar_dados(turmas, 'turmas.json')
        
        print("Turma apagada com sucesso!")
    else:
        print("Turma não encontrada.")