from database import conectar


def cadastrar_aluno(nome, idade, email):
    """
    Cadastra um novo aluno no banco de dados.
    """

    # Abre uma conexão com o banco MySQL
    conexao = conectar()

    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Comando SQL responsável por inserir um novo aluno
    sql = '''
    INSERT INTO alunos(nome, idade, email)
    VALUES (%s, %s, %s)
    '''

    # Agrupa os dados recebidos pela função
    valores = (nome, idade, email)

    # Executa o comando SQL enviando os valores
    cursor.execute(sql, valores)

    # Salva as alterações realizadas no banco
    conexao.commit()

    # Fecha o cursor após a execução
    cursor.close()

    # Fecha a conexão com o banco de dados
    conexao.close()

    # Informa ao usuário que o cadastro foi realizado
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    """
    Retorna todos os alunos cadastrados.
    """

    # Abre conexão com o banco
    conexao = conectar()

    # Cria cursor para executar consultas SQL
    cursor = conexao.cursor()

    # Consulta todos os alunos
    sql = "SELECT * FROM alunos"

    # Executa a consulta
    cursor.execute(sql)

    # Obtém todos os registros encontrados
    alunos = cursor.fetchall()

    # Fecha recursos utilizados
    cursor.close()
    conexao.close()

    return alunos