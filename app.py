alunos = []

while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Ver estatisticas")
    print("4 - Sair do programa")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("Cadastrar alunos")
            nome = input("Qual é o seu nome? ")
            idade = int(input("Qual é a sua idade? "))

            notas = []
            for i in range(1, 4):
                nota = float(input(f"Nota {i}? "))
                notas.append(nota)

            media = sum(notas) / 3
            print("A média do aluno", nome, "é", media)

            if media >= 7:
                print("Aprovado")
                situacao = "Aprovado"
            elif media >= 5:
                print("Recuperação")
                situacao = "Recuperacao"
            else:
                print("Reprovado")
                situacao = "Reprovado"

            aluno = {
                "nome": nome,
                "idade": idade,
                "notas": notas,
                "media": media,
                "situacao": situacao
            }

            alunos.append(aluno)
            print(f"Aluno {nome} cadastrado com sucesso.")

        case "2":
            print("Lista de alunos")
            if len(alunos) == 0:
                print("Nenhum aluno está cadastrado.")
            else:
                print("Lista de alunos:")
                for aluno in alunos:
                    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}, Media: {aluno['media']}, Situacao: {aluno['situacao']}")
        case "3":
            print("Ver estatísticas dos alunos")
            if len(alunos) == 0:
                print("Nenhum aluno está cadastrado.")
            else:
                maior_media = max(aluno['media'] for aluno in alunos)
                print("Maior média:", maior_media)

                print("Alunos aprovados:")
                aprovados = [aluno for aluno in alunos if aluno['situacao'] == "Aprovado"]

                if len(aprovados) == 0:
                    print("Nenhum aluno está aprovado.")
                else:
                    for aluno in aprovados:
                        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}, Média: {aluno['media']}, Situação: {aluno['situacao']}")

        case "4":
            print("Saindo do Programa. Até Logo!")
            break









