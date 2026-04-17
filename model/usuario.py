from database.conexao import conectar

# Criação com função:
# def inserir_usuario(usuario, senha):
#     """Função que cadastra o usuário"""

#     try:
#         conexao, cursor = conectar()
#         cursor.execute("INSERT INTO tb_usuario (usuario, senha) VALUES (%s, %s);", (usuario, senha))
#         conexao.commit()
#         conexao.close()
#         return True
    
#     except Exception as erro:
#         print(erro)
#         return False
    
# def verificar_login(usuario, senha):
#     """Função que verifica se o usuário está cadastrado"""


# Criação com classe:
class Usuario:
    def __init__(self, usuario:str, senha:str):
        self.usuario = usuario
        self.senha = senha
    
    def cadastrar(self):
        try:
            conexao, cursor = conectar()
            cursor.execute("INSERT INTO tb_usuario (usuario, senha) VALUES (%s, %s);", (self.usuario, self.senha))
            conexao.commit()
            conexao.close()
            return True
    
        except Exception as erro:
            print(erro)
            return False