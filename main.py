from database import conectar
from alunos import cadastrar_aluno

try:
    conexao = conectar()
    print("Conexão realizada com sucesso!")
    conexao.close()
except Exception as erro:
    print("Erro:", erro)
    
    from alunos import cadastrar_aluno

cadastrar_aluno(
    "Caio Sena",
    22,
    "caio@email.com"
)