from alunos import listar_alunos

# Busca todos os alunos cadastrados no banco
alunos = listar_alunos()

# Percorre cada aluno retornado pela consulta
for aluno in alunos:

    # Exibe os dados formatados para facilitar a leitura
    print(f"ID: {aluno[0]}")
    print(f"Nome: {aluno[1]}")
    print(f"Idade: {aluno[2]}")
    print(f"Email: {aluno[3]}")

    # Separador visual entre os registros
    print("-" * 30)