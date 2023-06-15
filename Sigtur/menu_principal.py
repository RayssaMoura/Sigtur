# Importe as funções dos arquivos correspondentes
from coordenador import menu_coordenador
from professor import menu_professor
from aluno import menu_aluno

# Função do menu principal
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
        print("| (0) - Sair do Sistema: Encerre sua sessão no SiGTur.                                                          |")
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

# Chame a função do menu principal para iniciar o programa
menu_principal()
