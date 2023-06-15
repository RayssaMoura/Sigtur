'''
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
        else:
            print("Aluno nao encontrado")

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
                print("Aluno não encontrado.")
            
    else:
        print("Opção inválida. Tente novamente.")'''