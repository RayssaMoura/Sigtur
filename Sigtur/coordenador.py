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
    
    if not professores:
        print("Não existe nenhum professor cadastrado.")
        return
    
    if len(alunos) < 2:
        if len(alunos) == 0:
            print("Não há nenhum aluno cadastrado.")
        else:
            print("Só há menos de dois alunos cadastrados para criar uma turma. É necessário pelo menos 2 alunos.")
        return
    
    print("Professores cadastrados:")
    for matricula, professor in professores.items():
        print("Matrícula:", matricula)
        print("Nome:", professor['nome'])
        print()
    
    professor_turma = escolher_professor()
    
    if professor_turma is None:
        print("Nenhum professor selecionado.")
        return
    
    print("Alunos cadastrados:")
    for aluno in alunos:
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Semestre: {aluno['semestre']}")
        print("----------")
    
    alunos_turma = escolher_alunos()
    
    while len(alunos_turma) < 2:
        opcao = input("Número insuficiente de alunos selecionados. Deseja adicionar mais alunos? (s/n): ")
        
        if opcao.lower() != 's':
            print("Turma não criada. Número mínimo de alunos não atingido.")
            return
        
        alunos_turma += escolher_alunos()
    
    turma = {
        'nome': nome_turma,
        'professor': professor_turma,
        'alunos': alunos_turma
    }
    
    turmas[nome_turma] = turma
    salvar_dados(turmas, 'turmas.json')
    
    print("Turma criada com sucesso!")


def editar_turma():
    if not turmas:
        print("Não há turmas cadastradas.")
        return
    
    print("Turmas cadastradas:")
    for nome_turma in turmas:
        print(nome_turma)
    
    nome_turma = input("Digite o nome da disciplina da turma a ser editada: ")
    
    if nome_turma in turmas:
        turma = turmas[nome_turma]
        
        opcao = input("Escolha uma opção:\nM - Mudar o professor da turma\nA - Adicionar aluno\nR - Remover aluno\nOpção: ")
        
        if opcao.lower() == 'm':
            professor = escolher_professor()
            turma['professor'] = professor
            print("Professor da turma alterado com sucesso!")
        elif opcao.lower() == 'a':
            alunos_turma = escolher_alunos()
            turma['alunos'] += alunos_turma
            print("Alunos adicionados à turma com sucesso!")
        elif opcao.lower() == 'r':
            if not turma['alunos']:
                print("Não há alunos na turma para remover.")
                return
            
            aluno_remover = escolher_alunos(turma['alunos'])
            
            if aluno_remover not in turma['alunos']:
                print("O aluno informado não está matriculado na turma.")
                return
            
            turma['alunos'].remove(aluno_remover)
            print("Aluno removido da turma com sucesso!")
        else:
            print("Opção inválida.")
            return
        
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
        opcao = input("Escolha a opção para selecionar o professor:\nM - Por matrícula\nN - Por nome\nOpção: ")
        
        if opcao.lower() == 'm':
            matricula = int(input("Digite a matrícula do professor desejado: "))
            
            if matricula in professores:
                professor = professores[matricula]
                print("Professor adicionado com sucesso!")
                return professor
            else:
                print("Professor não encontrado. Tente novamente.")
        elif opcao.lower() == 'n':
            nome = input("Digite o nome do professor desejado: ")
            
            for matricula, professor in professores.items():
                if professor['nome'].lower() == nome.lower():
                    print("Professor adicionado com sucesso!")
                    return professor
            
            print("Professor não encontrado. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

def escolher_alunos(alunos):
    while True:
        print("Alunos cadastrados:")
        for aluno in alunos:
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Semestre: {aluno['semestre']}")
            print("----------")
        
        opcao = input("Escolha a opção para selecionar o aluno:\nM - Por matrícula\nN - Por nome\nOpção: ")
        
        if opcao.lower() == 'm':
            matricula = input("Digite o número da matrícula do aluno: ")
            
            for aluno in alunos:
                if str(aluno['matricula']) == matricula:
                    print("Aluno adicionado com sucesso!")
                    return aluno
            
            print("Aluno não encontrado. Tente novamente.")
        
        elif opcao.lower() == 'n':
            nome = input("Digite o nome do aluno: ")
            
            for aluno in alunos:
                if aluno['nome'].lower() == nome.lower():
                    print("Aluno adicionado com sucesso!")
                    return aluno
            
            print("Aluno não encontrado. Tente novamente.")
        
        else:
            print("Opção inválida. Tente novamente.")

def ver_turma():
    if len(turmas) == 0:
        print("Nenhuma turma cadastrada.")
        return
    
    print("Turmas cadastradas:")
    for nome, turma in turmas.items():
        qtd_alunos = len(turma['alunos'])
        nome_professor = turma['professor']['nome']
        print(f"Turma: {nome} | Professor: {nome_professor} | Número de Alunos: {qtd_alunos}")
    
    nome_turma = input("Digite o nome da disciplina da turma a ser visualizada: ")
    
    if nome_turma in turmas:
        turma = turmas[nome_turma]
        print("Nome da turma:", turma['nome'])
        print("Professor da turma:", turma['professor']['nome'])
        print("Quantidade de alunos na turma:", len(turma['alunos']))
        print("Alunos da turma:")
        print("Nome\t\tMatricula\tSemestre")
        for aluno in turma['alunos']:
            print(f"{aluno['nome']}\t\t{aluno['matricula']}\t\t{aluno['semestre']}")
    else:
        print("Turma não encontrada.")

def apagar_turma():
    if len(turmas) == 0:
        print("Nenhuma turma cadastrada.")
        return
    
    print("Turmas cadastradas:")
    for nome in turmas:
        print(nome)
    
    nome_turma = input("Digite o nome da disciplina da turma a ser apagada: ")
    
    if nome_turma in turmas:
        del turmas[nome_turma]
        salvar_dados(turmas, 'turmas.json')
        
        print("Turma apagada com sucesso!")
    else:
        print("Turma não encontrada.")

def menu_coordenador():
    while True:
        print("\n+====================================Bem-vindo ao Menu do Coordenador!=================================================+")
        print("|...............Esperamos que o SiGTur facilite sua gestão e organize suas turmas de forma eficiente!..................|")
        print("|.....Aqui você encontrará todas as opções necessárias para gerenciar suas turmas de forma prática e organizada........|") 
        print("\n|--MENU COORDENADOR ---------------------------------------------------------------------------------------------------|")
        print("| (1) - Criar turma: Adicione uma nova turma, definindo nome, horários, professores e alunos associados.               |")
        print("| (2) - Editar turma: Faça alterações nas informações de uma turma existente, como horários, professores ou alunos.    |")
        print("| (3) - Ver turma: Visualize os detalhes de uma turma específica, incluindo horários, professores e alunos associados. |")
        print("| (4) - Apagar turma: Remova uma turma do sistema, excluindo todas as informações relacionadas a ela.                  |")
        print("| (0) - Voltar para o menu principal: Retorne ao menu principal para acessar outras funcionalidades do SiGTur.         |")
        print("-----------------------------------------------------------------------------------------------------------------------+")
        opcao = int(input(">>> Escolha uma das opções acima para começar :  "))
    
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

menu_coordenador()