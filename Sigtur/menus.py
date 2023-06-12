
# menu principal 
def menu_principal():
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


'''
        if opcao == '1':
            menu_coordenador()
        elif opcao == '2':
            menu_professor()
        elif opcao == '3':
            menu_aluno()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")'''

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
    
        
        
'''     if opcao == '1':
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
            print("Opção inválida. Tente novamente.")'''

def menu_professor():
    while True:
        print("\n+==========================================================Bem-vindo ao Menu Professor!================================================================+")
        print("|...........Aqui você terá acesso a todas as ferramentas necessárias para gerenciar as informacoes do professor........................................|")
        print("\n|--MENU PROFESSOR -------------------------------------------------------------------------------------------------------------------------------------|")
        print("| (1) - Cadastrar novo professor: Adicione um novo professor ao sistema, fornecendo detalhes como nome, contato e disciplina.                          |")
        print("| (2) - Editar professor cadastrado: Faça alterações nos dados de um professor já cadastrado, como informações de contato, nome ou disciplina.         |")
        print("| (3) - Ver dados de um professor cadastrado: Visualize todas as informações detalhadas de um professor específico.                                    |")
        print("| (4) - Excluir um professor cadastrado: Remova um professor do sistema, excluindo todas as informações relacionadas a ele.                            |")
        print("| (5) - Visualizar turmas de um professor específico: Veja todas as turmas associadas a um professor, incluindo horários, alunos e detalhes das turmas.|")
        print("| (6) - Visualizar os alunos da turma de um professor específico:Observe a lista de alunos matriculados em uma turma específica de um professor        |")
        print("| (0) - Voltar para o menu principal: Retorne ao menu principal para acessar outras funcionalidades do SiGTur.                                         |")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------+")
        opcao = input(">>> Escolha uma das opções acima:")
        
'''     if opcao == '1':
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
            print("Opção inválida. Tente novamente.")'''

def menu_aluno():
    while True:
        print("\n+=================================================Bem-vindo ao Menu Aluno!============================================================+")
        print("|......................Aqui você terá acesso a todas as opções para gerenciar as informações do aluno.................................|")
        print("\n|--MENU ALUNO ------------------------------------------------------------------------------------------------------------------------|")
        print("| (1) - Cadastrar novo aluno: Adicione um novo aluno ao sistema, fornecendo informações como nome, matrícula e contato.               |")
        print("| (2) - Editar aluno cadastrado: Faça alterações nos dados de um aluno já cadastrado, como informações de contato, nome ou matrícula. |")
        print("| (3) - Visualizar alunos cadastrados: Veja a lista completa de alunos cadastrados no sistema, com seus respectivos detalhes.         |")
        print("| (4) - Apagar aluno cadastrado: Remova um aluno do sistema, excluindo todas as informações relacionadas a ele.                       |")
        print("| (0) - Voltar para o menu principal: Retorne ao menu principal para acessar outras funcionalidades do SiGTur.                        |")
        print("--------------------------------------------------------------------------------------------------------------------------------------+")
        opcao = input(">>> Escolha uma das opções acima:")

        
'''     if opcao == '1':
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
            print("Opção inválida. Tente novamente.")'''

# Executar o programa
menu_aluno()