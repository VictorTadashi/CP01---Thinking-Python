alunos = []

while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Ver estatisticas")
    print("4 - Sair do programa")

    opcao = input("Escolha uma opcao: ")

    match opcao:
        case "1":
            print("Cadastrar alunos")
            nome = input("Qual e o seu nome? ")
            idade = int(input("Qual e a sua idade? "))

            notas = []
            for i in range(1, 4):
                nota = float(input(f"Qual e a sua nota {i}? "))
                notas.append(nota)

            media = sum(notas) / 3
            print("A media do aluno", nome, "e", media)

            if media >= 7:
                print("Aprovado")
                situacao = "Aprovado"
            elif media >= 5:
                print("Recuperacao")
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
            print(f"Aluno {nome} cadastrado com sucesso")

        case "2":
            print("Lista de alunos")
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado")
            else:
                print("Lista de alunos:")
                for aluno in alunos:
                    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}, Media: {aluno['media']}, Situacao: {aluno['situacao']}")
        case "3":
            print("Ver estatisticas dos alunos")
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado")
            else:
                maior_media = max(aluno['media'] for aluno in alunos)
                print("Maior media:", maior_media)

                print("Alunos aporvados:")
                aprovados = [aluno for aluno in alunos if aluno['situacao'] == "Aprovado"]

                if len(aprovados) == 0:
                    print("Nenhum aluno aprovado")
                else:
                    for aluno in aprovados:
                        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}, Media: {aluno['media']}, Situacao: {aluno['situacao']}")

        case "4":
            print("Sair do programa")
            break










