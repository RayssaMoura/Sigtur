'''
import json
professores = {}

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
    except: # se tiver algum erro no codigo acima quando rodado, executa o bloco a seguir
        return {}

# Carregar dados existentes (se houver) 
alunos = carregar_dados('alunos.json')
turmas = carregar_dados('turmas.json')

def cadastrar_professores(): 
    while True:
        nome_professor = input("- Digite o nome do Professor: ").upper() # recebe o nome do aluno e deixa todo maiusculo

        if not nome_professor.replace(" ", "").isalpha(): #verifica se o nome tem apenas caracteres alfabeticos, removendo todos os espacos em branco com o replace e dps usa o isalpha p verificar se tem apenas letras
            print("Erro: O nome deve conter apenas letras e espaços.") # se tiver numeros, aparece essa mensagem
        elif len(nome_professor.split()) < 2: #verifica se o nome tem menos de duas palavras, usando o split dividir em palavras e dps verifica se a quantidade de palavras è menor que 2
            print("Erro: O nome deve ser composto por nome e sobrenome.") # se for, retorna a msg de erro
        elif professor_existente(nome_professor): # verifica se um aluno com o nome digitado ja existe
            print("Erro: Já existe um aluno cadastrado com o mesmo nome.") # se existir aparece a msg de erro
        else:
            break # se nao para

    while True:
        disciplinas_ensinadas_prof = input("- Digite as disciplinas que o professor ensina: ") # recebe o numero da matricula

        if not disciplinas_ensinadas_prof.isalpha(): # verifica se foi digitado apenas letras
            print("Erro: As disciplinas devee ser apenas palavras e separadas por virgulas.") # se nao tiver sido, mostra a msg de erro
        else:
            break # se tiver sido digitado apenas letras, para
    
    matricula = gerar_matricula(professores) # recebe alunos como argumento e gera uma nova matricula
    dados = { # cria  o dicionario que vai ter as informacoes do aluno 
        'nome': nome_professor,
        'matricula': matricula,
        'disciplinas': disciplinas_ensinadas_prof,
        'turmas': []
    }
    professores[matricula] = dados 
    salvar_dados(professores, 'professores.json') 
    print(f"Professor(a) {nome_professor} de matrícula número {matricula} das disciplinas ( {disciplinas_ensinadas_prof} ), cadastrado com sucesso!")

def professor_existente(nome):  
    for professor in professores.values(): 
        if professor['nome'] == nome: 
            return True
    return False

def gerar_matricula(professores):
    matricula = len(professores) + 1
    return matricula 

cadastrar_professores()'''

import json
professores = {}

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

alunos = carregar_dados('professores.json')
turmas = carregar_dados('turmas.json')

def cadastrar_professor():
    while True:
        nome_professor = input("\n- Digite o nome do Professor: ").upper()

        if not nome_professor.replace(" ", "").isalpha():
            print("Erro: O nome deve conter apenas letras e espaços.")
        elif len(nome_professor.split()) < 2:
            print("Erro: O nome deve ser composto por nome e sobrenome.")
        elif professor_existente(nome_professor):
            print("Erro: Já existe um professor cadastrado com o mesmo nome.")
        else:
            break

    disciplinas_ensinadas_prof = input("- Digite as disciplinas que o professor ensina (separe por vírgula): ")
    disciplinas = [disciplina.strip() for disciplina in disciplinas_ensinadas_prof.split(',')]

    matricula = gerar_matricula(professores)
    dados = {
        'nome': nome_professor,
        'matricula': matricula,
        'disciplinas': disciplinas,
        'turmas': []
    }
    professores[matricula] = dados
    salvar_dados(professores, 'professores.json')
    print(f"Professor(a) {nome_professor} de matrícula número {matricula} das disciplinas ({', '.join(disciplinas)}), cadastrado com sucesso!")

def professor_existente(nome):
    for professor in professores.values():
        if professor['nome'] == nome:
            return True
    return False

def gerar_matricula(professores):
    matricula = len(professores) + 1
    return matricula

def editar_professor():
    if not professores:
        print("Não há professores cadastrados.")
        return

    print("Lista de professores cadastrados:")
    for matricula, professor in professores.items():
        print(f"Matrícula: {matricula}")
        print(f"Nome: {professor['nome']}")
        print(f"Disciplinas: {professor['disciplinas']}")
        print("----------")


    nome_ou_matricula_prof = input("\nDeseja editar por matrícula (M) ou por nome (N)? ").upper()
    
    if nome_ou_matricula_prof == "M":
        matricula = int(input("Digite a matrícula do professor a ser editado: "))
        
        if matricula in professores:
            professor = professores[matricula]
            nome_professor = input("\nDigite o novo nome do professor (ou pressione Enter para manter o mesmo): ")
            disciplinas_ensinadas_prof = input("Digite as novas disciplinas que o professor ensina (separe por vírgula) (ou pressione Enter para manter o mesmo): ")
            disciplinas = [disciplina.strip() for disciplina in disciplinas_ensinadas_prof.split(',')]
            
            professor['nome'] = nome_professor
            professor['disciplinas'] = disciplinas
            
            professores[matricula] = professor
            salvar_dados(professores, 'professores.json')
            
            print("Professor atualizado com sucesso!")
        else:
            print("Professor não encontrado.")
            
    elif nome_ou_matricula_prof == "N":
        nome_professor = input("Digite o nome do professor a ser editado: ").upper()
        
        for matricula, professor in professores.items():
            if professor['nome'] == nome_professor:
                novo_nome_professor = input("Digite o novo nome do professor (ou pressione Enter para manter o mesmo): ")
                disciplinas_ensinadas_prof = input("Digite as novas disciplinas que o professor ensina (separe por vírgula) (ou pressione Enter para manter o mesmo): ").upper()
                disciplinas = [disciplina.strip() for disciplina in disciplinas_ensinadas_prof.split(',')]
                
                professor['nome'] = novo_nome_professor
                professor['disciplinas'] = disciplinas
            
                professores[matricula] = professor
                salvar_dados(professores, 'professores.json')
                
                print("Professor atualizado com sucesso!")
                break
        
            else:
                print("Professor não encontrado.")
            
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
'''     elif opcao == '3':
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
            print("Opção inválida. Tente novamente.")'''

menu_professor()