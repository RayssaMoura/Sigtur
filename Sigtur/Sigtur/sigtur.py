import json 

# definindo os dics vazios que iracao armazenar info das turmas, professores e alunos
turmas = {}
professores = {}
alunos = {}

#dupla: breno inacio e rayssa mooura
# Observacao : funcao de ver dados do professor esta com um problema, pois quando apaga a turma do sistema ela continua aparecendoi nos dados, nao conseguimos corrogir

# criamos uma função para salvar os dados em um arquivo, usando json
def salvar_dados(dados, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(dados, f)

# criamos uma funcao para carregar os dados de um arquivo, usando json
def carregar_dados(arquivo):
    with open(arquivo, 'r') as file:
        return json.load(file)

# Carregar dados existentes (se houver) 
professores = carregar_dados("professores.json")
turmas = carregar_dados("turmas.json")
alunos = carregar_dados("alunos.json")
# =================================================== funcoes coordenador==================================================
def criar_turma():
    nome_turma = input("Digite o nome da disciplina: ").upper()
    
    if not professores:
        print("Não existe nenhum professor cadastrado.")
        return
    
    if len(alunos) < 2:
        if len(alunos) == 0:
            print("Não há nenhum aluno cadastrado.")
        else:
            print("Só há menos de dois alunos cadastrados para criar uma turma. É necessário pelo menos 2 alunos.")
        return  # Retorna para interromper a criação da turma
    
    professor_turma = escolher_professor()
    
    if professor_turma is None:
        print("Nenhum professor selecionado.")
        return  # Retorna para interromper a criação da turma
    
    alunos_turma = []
    escolher_alunos(alunos_turma)
    
    while len(alunos_turma) < 2:
        opcao = input("Número insuficiente de alunos selecionados. Deseja adicionar mais alunos? (s/n): ")

        if opcao.lower() != 's':
            print("Turma não criada. Número mínimo de alunos não atingido.")
            return  # Retorna para interromper a criação da turma
        escolher_alunos(alunos_turma)

        while True:
            opcao = input('Deseja adicionar mais alunos ? (s/n): ')

            if opcao.lower() != 's':
                break
            else:
                escolher_alunos(alunos_turma)

    turma = {
        'nome': nome_turma,
        'professor': professor_turma,
        'alunos': alunos_turma
    }
    
    turmas[nome_turma] = turma
    salvar_dados(turmas, 'turmas.json') 
    print("Turma criada com sucesso!")

    for professor in professores.values():
        if professor["nome"] == professor_turma["nome"]:
            professor["turmas"].append(nome_turma)
            salvar_dados(professores, "professores.json")

    for aluno in alunos.values():
        for nome in alunos_turma:
            if aluno["nome"] == nome['nome']:
                aluno["turmas"].append(nome_turma)
                salvar_dados(alunos, "alunos.json")

def buscar_por_matricula_prof(matricula): # definimos uma funcao pra buscar o prof pela matricula
    for professor in professores.values():
        if professor['matricula'] == matricula:
            return professor
    return None

def buscar_por_nome_prof(nome):  # definimos uma funcao pra buscar o prof pelo nome
    for professor in professores.values():
        if professor['nome'] == nome:
            return professor
    return None

def escolher_professor(): # definimos uma funcao pra escolher o prof
    print("Professores cadastrados:")
    for matricula, professor in professores.items():
        print("Matrícula:", matricula)
        print("Nome:", professor['nome'])
        print("-----------")

    while True:
        opcao = input("Escolha a opção para selecionar o professor, matrícula (M) ou por nome (N): ")

        if opcao.upper() == 'M':
            matricula = input("Digite a matrícula do professor desejado: ")
            if matricula.isdigit():
                return buscar_por_matricula_prof(int(matricula))
            else:
                print("A matrícula deve conter apenas números. Digite novamente.")

        elif opcao.upper() == 'N':
            nome = input("Digite o nome do professor desejado: ")
            if nome.replace(" ", "").isalpha():
                return buscar_por_nome_prof(nome)
            else:
                print("O nome deve conter apenas letras e espaços. Digite novamente.")
        else:
            print("Opção inválida. Tente novamente.")
            
def buscar_aluno_por_matricula(matricula): # definimos uma funcao pra buscar o aluno pelo nome
    for aluno in alunos.values():
        if aluno['matricula'] == matricula:
            print("Aluno selecionado com sucesso!")
            return aluno
    return None

def buscar_aluno_por_nome(nome): # definimos uma funcao pra buscar o nome pelo nome
    nome = nome.upper()
    for aluno in alunos.values():
        if aluno['nome'].upper() == nome:
            print("Aluno selecionado com sucesso!")
            return aluno
    return None

def escolher_alunos(alunos_turma): ## definimos uma funcao pra escolher os alunos
    while True:
        print("Alunos cadastrados:")
        for matricula, aluno in alunos.items():
            print(f"\nMatrícula: {matricula}")
            print(f"Nome: {aluno['nome']}")
            print(f"Semestre: {aluno['semestre']}")
            print("----------")
        
        opcao = input("\nEscolha a opção para selecionar o aluno, matrícula (M) ou por nome (N): ")
        
        if opcao.upper() == 'M':
            matricula = input("Digite o número da matrícula do aluno: ").upper()
            if matricula.isdigit():
                alunos_turma.append(buscar_aluno_por_matricula(int(matricula)))
                if alunos_turma is not None:
                    return alunos_turma  # Retorna uma lista com o aluno encontrado
                else:
                    print("Aluno não encontrado. Tente novamente.")
            else:
                print("A matrícula deve conter apenas números. Digite novamente.")
        
        elif opcao.upper() == 'N':
            nome = input("Digite o nome do aluno: ").upper()
            if nome.replace(" ", "").isalpha():
                aluno_encontrado = buscar_aluno_por_nome(nome)
                if aluno_encontrado is not None:
                    return [aluno_encontrado]  # Retorna uma lista com o aluno encontrado
                else:
                    print("Aluno não encontrado. Tente novamente.")
            else:
                print("O nome deve conter apenas letras e espaços. Digite novamente.")
        else:
            print("Opção inválida. Tente novamente.")

def escolher_alunos_remover(alunos_turma, turma): # definimos uma funcao pra escolher os alunos que deseja remover
    while True:
        print("Alunos cadastrados na turma:")
        for aluno in turma['alunos']:
            print("\nMatrícula:", aluno['matricula'])
            print("Nome:", aluno['nome'].upper())
            print("Semestre:", aluno['semestre'])
            print("----------")
       
        opcao = input("\nEscolha a opção para selecionar o aluno, matrícula (M) ou por nome (N): ")
        
        if opcao.upper() == 'M':
            matricula = input("Digite o número da matrícula do aluno: ")
            if matricula.isdigit():
                alunos_turma.append(buscar_aluno_por_matricula(int(matricula)))
                if alunos_turma is not None:
                    return alunos_turma  # Retorna uma lista com o aluno encontrado
                else:
                    print("Aluno não encontrado. Tente novamente.")
            else:
                print("A matrícula deve conter apenas números. Digite novamente.")
        
        elif opcao.upper() == 'N':
            nome = input("Digite o nome do aluno: ").upper()
            if nome.replace(" ", "").isalpha():
                aluno_encontrado = buscar_aluno_por_nome(nome)
                if aluno_encontrado is not None:
                    return [aluno_encontrado]  # Retorna uma lista com o aluno encontrado
                else:
                    print("Aluno não encontrado. Tente novamente.")
            else:
                print("O nome deve conter apenas letras e espaços. Digite novamente.")
        else:
            print("Opção inválida. Tente novamente.")

def editar_turma(): # definimos umaa funcao pra editar a turma
    if not turmas:
        print("Não há turmas cadastradas.")
        return
    
    print("Turmas cadastradas:")
    for nome_turma in turmas:
        print(nome_turma)
    
    nome_turma = input("Digite o nome da disciplina da turma a ser editada: ").upper()
    
    if nome_turma in turmas:
        turma = turmas[nome_turma]
        
        opcao = input("Escolha uma opção: (M) - Mudar o professor da turma, (A) - Adicionar aluno ou (R) - Remover aluno: ")
        
        if opcao.lower() == 'm':
            professor = escolher_professor()
            turma['professor'] = professor
            print("Professor da turma alterado com sucesso!")
        elif opcao.lower() == 'a':
            alunos_turma = []
            escolher_alunos(alunos_turma)
            if turma['alunos'] == alunos_turma:
                print('Esse aluno já está na turma')
            else:
                turma['alunos'] += alunos_turma
                print("Alunos adicionados à turma com sucesso!")
        elif opcao.lower() == 'r':
            if not turma['alunos']:
                print("Não há alunos na turma para remover.")
                return
            
            aluno_remover = []
            escolher_alunos_remover(aluno_remover, turma) # tirei o parametro turma['alunos']

            for i in aluno_remover:
                if i not in turma['alunos']:
                    print('O aluno informado não está matrículado na turma.')
                else:
                    for c in turma['alunos']:
                        if c == i:
                            turma['alunos'].remove(c)
                            print("Aluno removido da turma com sucesso!")
        else:
            print("Opção inválida.")
            return
        
        turmas[nome_turma] = turma
        salvar_dados(turmas, 'turmas.json')
        
        print("Turma atualizada com sucesso!")
    else:
        print("Turma não encontrada.")

def ver_turma(): # definimos uma funcao pra ver a turma
    if len(turmas) == 0:
        print("Nenhuma turma cadastrada.")
        return

    print("Turmas cadastradas:")
    for nome in turmas:
        print(nome)

    nome_turma = input("\nDigite o nome da disciplina da turma que você deseja visualizar: ").upper()

    if nome_turma in turmas:
        turma = turmas[nome_turma]
        professor = turma['professor']
        alunos_turma = turma['alunos']

        print("\nNome da turma:", nome_turma)
        print("Professor da turma:", professor['nome'])
        print("Quantidade de alunos na turma:", len(alunos_turma))
        print("Alunos matriculados na turma:")
        print("\nNome\t\t\tMatrícula\tSemestre")
        for aluno in alunos_turma:
            print(f"{aluno['nome']}\t\t{aluno['matricula']}\t\t{aluno['semestre']}")
    else:
        print("Turma não encontrada.")

def apagar_turma(): # definimos uma funcao pra apagaar a turma
    if len(turmas) == 0:
        print("Nenhuma turma cadastrada.")
        return
    
    print("Turmas cadastradas:")
    for nome in turmas:
        print(nome)
    
    nome_turma = input("Digite o nome da disciplina da turma a ser apagada: ").upper()
    
    if nome_turma in turmas:
        del turmas[nome_turma]
        salvar_dados(turmas, 'turmas.json')
        
        print("Turma apagada com sucesso!")
    else:
        print("Turma não encontrada.")

def menu_coordenador(): # definimos o menu do coordenador
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
    
        if opcao == 1:
            criar_turma()
        elif opcao == 2:
            editar_turma()
        elif opcao == 3:
            ver_turma()
        elif opcao == 4:
            apagar_turma()
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")
#============================================= funcoes professor ==============================================
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

    disciplinas_ensinadas_prof = input("- Digite as disciplinas que o professor ensina (separe por vírgula): ").upper()
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

def professor_existente(nome): # definimos uma funcao pra verificar se o professor ja existe
    for professor in professores.values():
        if professor['nome'] == nome:
            return True
    return False

def gerar_matricula(professores): # definimos uma funcao pra gerar matriucula
    matricula = len(professores) + 1
    return matricula

def editar_professor(): # definimos uma funcao pra editar o professor
    if not professores:
        print("Não há professores cadastrados.")
        return

    print("Lista de professores cadastrados:")
    for matricula, professor in professores.items():
        print(f"\nMatrícula: {matricula}")
        print(f"Nome: {professor['nome']}")
        print(f"Disciplinas: {professor['disciplinas']}")
        print("----------")

    while True:
        nome_ou_matricula_prof = input("\nDeseja editar por matrícula (M) ou por nome (N)? ").upper()

        if nome_ou_matricula_prof == "M":
            while True:
                matricula = input("Digite a matrícula do professor a ser editado (ou pressione Enter para voltar): ")
                if matricula.strip() == "":
                    break
                if matricula.isdigit():
                    matricula = int(matricula)
                    professor = buscar_por_matricula_prof(matricula)
                    if professor:
                        nome_professor = input("\nDigite o novo nome do professor (ou pressione Enter para manter o mesmo): ").upper()
                        if nome_professor.strip() != "":
                            professor['nome'] = nome_professor

                        while True:
                            disciplinas_opcao = input("Digite 'A' para adicionar uma disciplina, 'E' para editar uma disciplina, 'EX' para excluir uma disciplina ou 'N' para não editar nada: ").upper()
                            if disciplinas_opcao == "A":
                                disciplina_adicionar = input("Digite a disciplina a ser adicionada: ").upper()
                                if disciplina_adicionar.strip() != "":
                                    professor['disciplinas'].append(disciplina_adicionar)
                                    print("Disciplina adicionada.")
                                else:
                                    print("Nada foi digitado. Digite novamente ou pressione Enter.")
                            elif disciplinas_opcao == "E":
                                disciplina_antiga = input("Digite a disciplina a ser editada: ").upper()
                                if disciplina_antiga.strip() != "":
                                    if disciplina_antiga in professor['disciplinas']:
                                        disciplina_nova = input("Digite a nova disciplina: ").upper()
                                        if disciplina_nova.strip() != "":
                                            index = professor['disciplinas'].index(disciplina_antiga)
                                            professor['disciplinas'][index] = disciplina_nova
                                            print("Disciplina editada.")
                                        else:
                                            print("Nada foi digitado. Digite novamente ou pressione Enter.")
                                    else:
                                        print("Disciplina não encontrada. Por favor, digite novamente.")
                                else:
                                    print("Nada foi digitado. Digite novamente ou pressione Enter.")
                            elif disciplinas_opcao == "EX":
                                disciplina_excluir = input("Digite a disciplina a ser excluída: ").upper()
                                if disciplina_excluir.strip() != "":
                                    if disciplina_excluir in professor['disciplinas']:
                                        professor['disciplinas'].remove(disciplina_excluir)
                                        print("Disciplina excluída.")
                                    else:
                                        print("Disciplina não encontrada. Por favor, digite novamente.")
                                else:
                                    print("Nada foi digitado. Digite novamente ou pressione Enter.")
                            elif disciplinas_opcao == "N":
                                break
                            else:
                                print("Opção inválida. Por favor, digite novamente.")
                    else:
                        print("Professor não encontrado.")
                else:
                    print("A matrícula deve conter apenas números. Digite novamente ou pressione Enter.")

        elif nome_ou_matricula_prof == "N":
            while True:
                nome_professor = input("Digite o nome do professor a ser editado (ou pressione Enter para voltar): ").upper()
                if nome_professor.strip() == "":
                    break
                if nome_professor.replace(" ", "").isalpha():
                    professor = buscar_por_nome_prof(nome_professor)
                    if professor:
                        novo_nome_professor = input("Digite o novo nome do professor (ou pressione Enter para manter o mesmo): ").upper()
                        if novo_nome_professor.strip() != "":
                            professor['nome'] = novo_nome_professor

                        while True:
                            disciplinas_opcao = input("Digite 'A' para adicionar uma disciplina, 'E' para editar uma disciplina, 'D' para excluir uma disciplina ou 'N' para não fazer nada: ").upper()

                            if disciplinas_opcao == "A":
                                disciplina_adicionar = input("Digite a disciplina a ser adicionada: ").upper()
                                if disciplina_adicionar.strip() != "":
                                    professor['disciplinas'].append(disciplina_adicionar)
                                    print("Disciplina adicionada.")
                                else:
                                    print("Nada foi digitado. ")
                            elif disciplinas_opcao == "E":
                                disciplina_antiga = input("Digite a disciplina a ser editada: ").upper()
                                if disciplina_antiga.strip() != "":
                                    if disciplina_antiga in professor['disciplinas']:
                                        disciplina_nova = input("Digite a nova disciplina: ").upper()
                                        if disciplina_nova.strip() != "":
                                            index = professor['disciplinas'].index(disciplina_antiga)
                                            professor['disciplinas'][index] = disciplina_nova
                                            print("Disciplina editada.")
                                        else:
                                            print("Nada foi digitado.")
                                    else:
                                        print("Disciplina não encontrada. Por favor, digite novamente.")
                                else:
                                    print("Nada foi digitado. ")
                            elif disciplinas_opcao == "EX":
                                disciplina_excluir = input("Digite a disciplina a ser excluída: ").upper()
                                if disciplina_excluir.strip() != "":
                                    if disciplina_excluir in professor['disciplinas']:
                                        professor['disciplinas'].remove(disciplina_excluir)
                                        print("Disciplina excluída.")
                                    else:
                                        print("Disciplina não encontrada. Por favor, digite novamente.")
                                else:
                                    print("Nada foi digitado.")
                            elif disciplinas_opcao == "N":
                                break
                            else:
                                print("Opção inválida. Por favor, digite novamente.")
                else:
                    print("O nome deve conter apenas letras e espaços. Digite novamente ou pressione Enter.")

        else:
            print("Opção inválida. Tente novamente.")
        continuar = input("Deseja fazer mais alguma edição? (S/N) ").upper()
        if continuar == "N":
            break
    print("Professor atualizado com sucesso!")

def ver_dados_professor(): # definimos uma funcao pra ver os dados do professor
    if not professores:
        print("Não há professores cadastrados.")
        return

    print("Lista de professores cadastrados:")
    for matricula, professor in professores.items():
        print(f"Matrícula: {matricula}")
        print(f"Nome: {professor['nome']}")
        print(f"Disciplinas: {professor['disciplinas']}")
        print("----------")

    nome_ou_matricula = input("\nDeseja visualizar por matrícula (M) ou por nome (N)? ").upper()

    if nome_ou_matricula == "M":
        while True:
            matricula = input("Digite a matrícula do professor a ser visualizado: ")
            if matricula.isdigit():
                matricula = matricula
                if matricula in professores:
                    professor = professores[matricula]
                    print("Matrícula:", professor['matricula'])
                    print("Nome:", professor['nome'])
                    print("Disciplinas que o professor ensina:")
                    for disciplina in professor['disciplinas']:
                        print("-", disciplina)
                    print("Turmas em que o professor leciona:")
                    for turma in professor['turmas']:
                        print("-", turma)
                    break
                else:
                    print("Professor não encontrado.")
            else:
                print("A matrícula deve conter apenas números. Digite novamente.")

    elif nome_ou_matricula == "N":
        while True:
            nome_professor = input("Digite o nome do professor a ser visualizado: ").upper()
            encontrou_professor = False
            for matricula, professor in professores.items():
                if professor['nome'].upper() == nome_professor:
                    print("Matrícula:", professor['matricula'])
                    print("Nome:", professor['nome'])
                    print("Disciplinas que o professor ensina:")
                    for disciplina in professor['disciplinas']:
                        print("-", disciplina)
                    print("Turmas em que o professor leciona:")
                    for turma in professor['turmas']:
                        print("-", turma)
                    encontrou_professor = True
                    break

            if not encontrou_professor:
                print("Professor não encontrado.")
            break
        else:
            print("O nome deve conter apenas letras e espaços. Digite novamente.")
    else:
        print("Opção inválida. Tente novamente.")

def excluir_professor(): # definimos uma funcao pra excluir o professor
    if not professores:
        print("Não há professores cadastrados.")
        return
    
    print("\nLista de professores:")
    for matricula, professor in professores.items():
        print("\nMatrícula:", matricula)
        print("Nome:", professor['nome'])
        print(f"Disciplinas: {professor['disciplinas']}")
        print("----------")

    nome_ou_matricula_prof = input("\nDeseja excluir por matrícula (M) ou por nome (N)? ").upper()

    if nome_ou_matricula_prof == 'M':
        while True:
            matricula = input("Digite a matrícula do professor a ser apagado: ")
            if matricula.isdigit():
                matricula = matricula.upper()
                if matricula in professores:
                    del professores[matricula]
                    salvar_dados(professores, 'professores.json')
                    print(f"Professor com matrícula {matricula} apagado com sucesso!")
                    break
                else:
                    print("Professor não encontrado.")
            else:
                print("A matrícula deve conter apenas números. Digite novamente.")

    elif nome_ou_matricula_prof == 'N':
        while True:
            nome = input("Digite o nome do professor a ser apagado: ").upper()
            if nome.replace(" ", "").isalpha():
                encontrou_professor = False
                for matricula, professor in professores.items():
                    if professor['nome'].upper() == nome:
                        del professores[matricula]
                        salvar_dados(professores, 'professores.json')
                        print(f"Professor com nome {nome} apagado com sucesso!")
                        encontrou_professor = True
                        break

                if not encontrou_professor:
                    print("Professor não encontrado.")
                break
            else:
                print("O nome deve conter apenas letras e espaços. Digite novamente.")

    else:
        print("Opção inválida.")

def visualizar_turmas_professor(): # definimos vizualizar as turmas de um professor
    print("\nLista de professores:")
    for matricula, professor in professores.items():
        print("\nMatrícula:", matricula)
        print("Nome:", professor['nome'])
        print(f"Disciplinas: {professor['disciplinas']}")
        print("----------")
    
    nome_ou_matricula_prof = input("\nDeseja visualizar turmas por matrícula (M) ou por nome (N)? ").upper()

    if nome_ou_matricula_prof == 'M':
        while True:
            matricula_prof = input("Digite a matrícula do professor: ")
            if matricula_prof.isdigit():
                turmas_professor = [turma_nome 
                                    for turma_nome, turma in turmas.items() 
                                    if turma['professor']['matricula'] == int(matricula_prof)]
                break
            else:
                print("A matrícula deve conter apenas números. Digite novamente.")

    elif nome_ou_matricula_prof == 'N':
        while True:
            nome_prof = input("Digite o nome do professor: ")
            if nome_prof.replace(" ", "").isalpha():
                turmas_professor = [turma_nome for turma_nome, turma in turmas.items() if turma['professor']['nome'].lower() == nome_prof.lower()]
                break
            else:
                print("O nome deve conter apenas letras e espaços. Digite novamente.")

    else:
        print("Opção inválida.")
        return
    
    if len(turmas_professor) > 0:
        print("\nTurmas vinculadas ao professor:")
        for turma_nome in turmas_professor:
            print(turma_nome)
    else:
        print("\nNenhuma turma encontrada para o professor.")

def visualizar_alunos_da_turma_de_um_prof_especifico(): # definimos uma funcao para vizualizar as turmas de um prof especifico
    print("Professores cadastrados:") # exibe a lista de professores cadastrados 
    for matricula, professor in professores.items():
        print("\nMatrícula:", matricula)
        print("Nome:", professor['nome'])
        print(f"Disciplinas: {professor['disciplinas']}")
        print("----------")
    
    while True:
        nome_ou_matricula_prof = input("\nDeseja visualizar por matrícula (M) ou por nome (N)? ").upper() #pede pra vc escolher
        
        if nome_ou_matricula_prof == 'M': # se a opção for matricula
            while True:
                matricula_prof = input("Digite a matrícula do professor(a) (apenas números): ") # solicita a matricula do professor.
                
                if not matricula_prof.isdigit():
                    print("A matrícula deve conter apenas números.")
                    continue
                
                professor_encontrado = False
                for matricula, professor in professores.items():
                    if matricula_prof == str(matricula):
                        professor_encontrado = True
                        nome_professor = professor['nome']
                        break
                
                if not professor_encontrado:
                    print("Professor não encontrado.")
                
                turmas_do_professor = [nome_turma for nome_turma, turma in turmas.items() if turma['professor']['nome'] == nome_professor]
                
                if not turmas_do_professor:
                    print(f"O professor(a) {nome_professor} não está associado a nenhuma turma.")
                    resposta = input("Deseja visualizar turmas de outro professor(a)? (S/N): ")
                    if resposta.upper() == 'N':
                        break
                    continue
               
                print(f"Turmas do professor(a) {nome_professor}:")
                for nome_turma in turmas_do_professor:
                    print(nome_turma)
                
                while True:
                    nome_turma = input("Digite o nome da turma: ").upper()
                    
                    if nome_turma not in turmas_do_professor:
                        print("Turma não encontrada.")
                        resposta = input("Deseja visualizar alunos de outra turma? (S/N): ")
                        if resposta.upper() == 'N':
                            break
                        continue
                    
                    turma = turmas[nome_turma]
                    print(f"\nTurma: {nome_turma}")
                    print("Alunos:")
                    print("Matrícula - Nome")
                    for aluno in turma['alunos']:
                        print(f"{aluno['matricula']} - {aluno['nome']}")
                    
                    resposta = input("\nDeseja visualizar mais alguma turma? (S/N): ")
                    if resposta.upper() == 'S':
                        visualizar_alunos_da_turma_de_um_prof_especifico()
                    else:
                        break
                
                resposta = input("Deseja visualizar turmas de outro professor(a)? (S/N): ")
                if resposta.upper() == 'N':
                    menu_professor()
        
        elif nome_ou_matricula_prof == 'N': # por nome
            while True:
                nome_professor = input("Digite o nome do professor(a) (apenas letras): ").upper() 
                
                if not nome_professor.replace(" ", "").isalpha(): # verificao de que apenas letras foram digitadas
                    print("O nome deve conter apenas letras.")
                    continue

                professor_encontrado = False
                for matricula, professor in professores.items(): 
                    if nome_professor.upper() == professor['nome'].upper():
                        professor_encontrado = True
                        nome_professor = professor['nome']
                        break
                
                if not professor_encontrado:
                    print("Professor não encontrado.")
                    resposta = input("Deseja visualizar turmas de outro professor(a)? (S/N): ")
                    if resposta.upper() == 'N':
                        break
                    continue
                
                turmas_do_professor = [nome_turma for nome_turma, turma in turmas.items() if turma['professor']['nome'] == nome_professor]
                
                if not turmas_do_professor:
                    print(f"O professor {nome_professor} não está associado a nenhuma turma.")
                    resposta = input("Deseja visualizar turmas de outro professor(a)? (S/N): ")
                    if resposta.upper() == 'N':
                        break
                    continue
                
                print(f"Turmas do professor(a) {nome_professor}:")
                for nome_turma in turmas_do_professor:
                    print(nome_turma)
                
                while True:
                    nome_turma = input("Digite o nome da turma: ").upper()
                    
                    if nome_turma not in turmas_do_professor:
                        print("Turma não encontrada.")
                        resposta = input("Deseja visualizar alunos de outra turma? (S/N): ")
                        if resposta.upper() == 'N':
                            break
                        continue
                    
                    turma = turmas[nome_turma]
                    print(f"\nTurma: {nome_turma}")
                    print("Alunos:")
                    print("Matrícula - Nome")
                    for aluno in turma['alunos']:
                        print(f"{aluno['matricula']} - {aluno['nome']}")
                    
                    resposta = input("\nDeseja visualizar mais alguma turma? (S/N): ")
                    if resposta.upper() == 'S':
                        visualizar_alunos_da_turma_de_um_prof_especifico()
                    else:
                        break
                
                resposta = input("Deseja visualizar turmas de outro professor(a)? (S/N): ")
                if resposta.upper() == 'N':
                    menu_professor()
        else:
            print("Opção inválida. Digite 'M' para exclusão por matrícula ou 'N' para exclusão por nome.")
            continue
        break

def menu_professor(): #definimos o menu prof
    while True:
        print("\n+==========================================================Bem-vindo ao Menu Professor!================================================================+")
        print("|...........Aqui você terá acesso a todas as ferramentas necessárias para gerenciar as informacoes do professor........................................|")
        print("\n|--MENU PROFESSOR -------------------------------------------------------------------------------------------------------------------------------------|")
        print("| (1) - Cadastrar novo professor: Adicione um novo professor ao sistema, fornecendo detalhes como nome e disciplina.                                   |")
        print("| (2) - Editar professor cadastrado: Faça alterações nos dados de um professor já cadastrado, como informações de nome ou disciplina.                  |")
        print("| (3) - Ver dados de um professor cadastrado: Visualize todas as informações detalhadas de um professor específico.                                    |")
        print("| (4) - Excluir um professor cadastrado: Remova um professor do sistema, excluindo todas as informações relacionadas a ele.                            |")
        print("| (5) - Visualizar turmas de um professor específico: Veja todas as turmas associadas a um professor, alunos e detalhes das turmas.                    |")
        print("| (6) - Visualizar os alunos da turma de um professor específico:Observe a lista de alunos matriculados em uma turma específica de um professor        |")
        print("| (0) - Voltar para o menu principal: Retorne ao menu principal para acessar outras funcionalidades do SiGTur.                                         |")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------+")
        opcao = input(">>> Escolha uma das opções acima: ")
        
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
            visualizar_alunos_da_turma_de_um_prof_especifico()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
# ===========================================================Funções  Aluno===========================================
def cadastrar_aluno(): #definimos a funcao de cadastro de alunos
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

def gerar_matricula(alunos): # definimos uma funcao p gerar a MATRICULa do aluno
    matricula = len(alunos.keys()) + 1
    return matricula 

def editar_aluno(): # definimos uma funcao pra editar aluno
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

def visualizar_alunos(): # definimos uma funcao para vizualizar os alunos cadastrados
    if not alunos: # se nao tiver nenhum aluno cadastrado,
        print("Nenhum aluno cadastrado.") # mostra a mensagem
        return

    print("\nAlunos cadastrados:\n") # se tiver, mostra a lista de aluinos, com as informacoes sobre eles 
    for matricula, aluno in alunos.items():
        print("Matrícula:", matricula)
        print("Nome:", aluno['nome'])
        print(f"Semestre: {aluno['semestre']}")
        print("----------")

def apagar_aluno(): # deefinimos uma funcao pra apagar aluno
    if not alunos: # Verifica se tem alunos cadastrados 
        print("Não há alunos cadastrados.")
        return
    
    print("\nLista de alunos:") # exibe a lista de alunos.
    for matricula, aluno in alunos.items():
        print("\nMatrícula:", matricula)
        print("Nome:", aluno['nome'])
        print(f"Semestre: {aluno['semestre']}")
        print("----------")

    nome_ou_matricula = input("\nDeseja apagar por matrícula (M) ou por nome (N)? ").upper() #pergunta se vc deseja apagar o aluno por matricula ou por nome

    if nome_ou_matricula == 'M':
        while True:
            matricula = input("Digite a matrícula do aluno a ser apagado: ") # pede a matricula do aluno a ser apagado.
            if matricula.isdigit():
                if matricula in alunos:
                    del alunos[matricula] # executa a exclusão do aluno escolhido.
                    salvar_dados(alunos, 'alunos.json')
                    print(f"Aluno com matrícula {matricula} apagado com sucesso!")
                    break
                else:
                    print("Aluno não encontrado.")
            else:
                print("A matrícula deve conter apenas números. Digite novamente.")
                
    elif nome_ou_matricula == 'N':
        while True:
            nome = input("Digite o nome do aluno a ser apagado: ").upper() #solicita o nome do aluno a ser apagado.
            if nome.replace(" ", "").isalpha():
                encontrou_aluno = False
                for matricula, aluno in alunos.items():
                    if aluno['nome'].upper() == nome:
                        del alunos[matricula] #  o aluno é removido
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

def menu_aluno(): # definimos o menu aluno
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

def menu_principal(): # definimos o menu principal
    while True:
        print("\n+===========================Bem-vindo ao SiGTur - Sistema de Gestão de Turmas!==================================+")
        print("|............Nosso objetivo é tornar a gestão das suas turmas mais eficiente e descomplicada!...................|")
        print("|...................Utilize o SiGTur e aproveite todas as funcionalidades disponíveis!..........................|")
        print("\n| Aqui no menu principal, você terá acesso a todas as funcionalidades do SiGTur                                 |") 
        print("\n|--MENU PRINCIPAL ----------------------------------------------------------------------------------------------|")
        print("| (1) - Coordenador: Gerencie as turmas, crie, edite, visualize e apague informações.                           |")
        print("| (2) - Professor: Cadastre e gerencie os dados dos professores, visualize turmas e alunos associados.          |")
        print("| (3) - Aluno: Cadastre e gerencie os alunos, visualize e edite suas informações.                               |")
        print("| (0) - Sair do Sitema: Encerre sua sessão no SiGTur.                                                           |")
        print("----------------------------------------------------------------------------------------------------------------+")
        opcao = int(input(">>> Escolha uma das opções acima para começar a gerenciar suas turmas de forma eficiente:  "))

        if opcao == 1:
            menu_coordenador()
        elif opcao == 2:
            menu_professor()
        elif opcao == 3:
            menu_aluno()
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()