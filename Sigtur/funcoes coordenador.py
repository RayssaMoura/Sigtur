import json
professores = {}
turmas = {} 


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

def cadastrar_professor(): 
    while True:
        nome_professor = input("- Digite o nome do Professor(a): ").upper() 

        if not nome_professor.replace(" ", "").isalpha(): 
            print("Erro: O nome deve conter apenas letras e espaços.") 
        elif len(nome_professor.split()) < 2: 
            print("Erro: O nome deve ser composto por nome e sobrenome.") 
        elif professor_existente(nome_professor): 
            print("Erro: Já existe um professor cadastrado com o mesmo nome.") 
        else:
            break 

    while True:
        disciplinas_ensinadas_p_professor = input("- Digite as materias que o profesor ensina: ") 

        if not disciplinas_ensinadas_p_professor.replace(" ", "").isalpha(): 
            print("Erro: As materias devem contem apenas letras.") 
        else:
            break
    
    matricula = gerar_matricula(professores) # recebe alunos como argumento e gera uma nova matricula
    dados = { # cria  o dicionario que vai ter as informacoes do aluno 
        'nome': nome_professor,
        'matricula': matricula,
        'Disciplinas': disciplinas_ensinadas_p_professor,
        'turmas': []
    }
    professores[matricula] = dados 
    salvar_dados(professores, 'alunos.json') 
    print(f"Professor(a) {nome_professor} de matrícula número {matricula} das disciplinas: {disciplinas_ensinadas_p_professor}, cadastrado com sucesso!")

def professor_existente(nome): 
    for professor in professores.values(): 
        if professor['nome'] == nome: 
            return True
    return False

def gerar_matricula(professores):
    matricula = len(professores) + 1 
    return matricula 

cadastrar_professor()

'''
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
        print("Turma não encontrada.")'''