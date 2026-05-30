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