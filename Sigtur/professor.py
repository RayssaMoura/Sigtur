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
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não está no formato JSON válido.")
        return {}

alunos = carregar_dados('professores.json')

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

                    if matricula in professores:
                        professor = professores[matricula]
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
                    encontrou_professor = False

                    for matricula, professor in professores.items():
                        if professor['nome'] == nome_professor:
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

                            encontrou_professor = True
                            break

                    if not encontrou_professor:
                        print("Professor não encontrado.")
                else:
                    print("O nome deve conter apenas letras e espaços. Digite novamente ou pressione Enter.")

        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("Deseja fazer mais alguma edição? (S/N) ").upper()
        if continuar == "N":
            break

    print("Professor atualizado com sucesso!")

def ver_dados_professor():
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
                matricula = int(matricula)
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
            if nome_professor.replace(" ", "").isalpha():
                encontrou_professor = False
                for matricula, professor in professores.items():
                    if professor['nome'] == nome_professor:
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

'''
def excluir_professor():
    if not professores:
        print("Não há professores cadastrados.")
        return
    
    print("\nLista de professores:")
    for matricula, professor in professores.items():
        print("\nMatrícula:", matricula)
        print("Nome:", professor['nome'])
        print(f"Disciplinas: {professor['disciplinas']}")
        print("----------")

    nome_ou_matricula_prof = input("\nDeseja editar por matrícula (M) ou por nome (N)? ").upper()

    if nome_ou_matricula_prof == 'M':
        matricula = input("Digite a matrícula do professor a ser apagado: ").upper()
        if matricula in professores.keys():
            del professores[matricula]
            salvar_dados(professores, 'professores.json')
            print(f"Professor com matrícula {matricula} apagado com sucesso!")
        else:
            print("Professor não encontrado.")
    elif nome_ou_matricula_prof == 'N':
        nome = input("Digite o nome do professor a ser apagado: ").upper()
        for matricula, professor in professores.items():
            if professor['nome'].lower() == nome.lower():
                del professores[matricula]
                salvar_dados(professores, 'professores.json')
                print(f"Professor com nome {nome} apagado com sucesso!")
                break
            else:
                print("Professor não encontrado.")
    else:
        print("Opção inválida.")'''

def excluir_professor():
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

def visualizar_turmas_professor():
    print("\nLista de professores:")
    for matricula, professor in professores.items():
        print("\nMatrícula:", matricula)
        print("Nome:", professor['nome'])
        print(f"Disciplinas: {professor['disciplinas']}")
    
    nome_ou_matricula_prof = input("\nDeseja visualizar turmas por matrícula (M) ou por nome (N)? ").upper()

    if nome_ou_matricula_prof == 'M':
        while True:
            matricula_prof = input("Digite a matrícula do professor: ")
            if matricula_prof.isdigit():
                turmas_professor = [turma_nome for turma_nome, turma in turmas.items() if turma['professor']['matricula'] == matricula_prof]
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

def visualizar_alunos_turma_professor():
    print("Turmas cadastradas:")
    for nome_turma in turmas:
        print(nome_turma)
    
    nome_turma = input("Digite o nome da turma: ")
    
    if nome_turma in turmas:
        turma = turmas[nome_turma]
        print("Alunos da turma:")
        for aluno in turma['alunos']:
            print(aluno['nome'])
    else:
        print("Turma não encontrada.")

def menu_professor():
    while True:
        print("\n+==========================================================Bem-vindo ao Menu Professor!================================================================+")
        print("|...........Aqui você terá acesso a todas as ferramentas necessárias para gerenciar as informacoes do professor........................................|")
        print("\n|--MENU PROFESSOR -------------------------------------------------------------------------------------------------------------------------------------|")
        print("| (1) - Cadastrar novo professor: Adicione um novo professor ao sistema, fornecendo detalhes como nome e disciplina.                                   |")
        print("| (2) - Editar professor cadastrado: Faça alterações nos dados de um professor já cadastrado, como informações de nome ou disciplina.                  |")
        print("| (3) - Ver dados de um professor cadastrado: Visualize todas as informações detalhadas de um professor específico.                                    |")
        print("| (4) - Excluir um professor cadastrado: Remova um professor do sistema, excluindo todas as informações relacionadas a ele.                            |")
        print("| (5) - Visualizar turmas de um professor específico: Veja todas as turmas associadas a um professor, incluindo horários, alunos e detalhes das turmas.|")
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
            visualizar_alunos_turma_professor()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_professor()
