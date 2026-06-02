from database import conectar


def cadastrar_aluno(nome, idade, email):
    
    conexao = conectar()
    
    cursor = conexao.cursor()
    
    sql = '''
    Insert into alunos(nome, idade, email)
    Values (%s,%s,%s)
    '''
    
    valores = (nome, idade, email) 
    
    cursor.execute(sql, valores)
    
    conexao.commit()
    
    cursor.close()
    
    conexao.close()
    
    print("aluno cadastrado com sucesso")
    
    
from database import conectar


def cadastrar_aluno(nome, idade, email):
    """
    Cadastra um novo aluno no banco de dados.
    """

    conexao = conectar()

    cursor = conexao.cursor()

    sql = '''
    INSERT INTO alunos(nome, idade, email)
    VALUES (%s, %s, %s)
    '''

    valores = (nome, idade, email)

    cursor.execute(sql, valores)

    conexao.commit()

    cursor.close()
    conexao.close()

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