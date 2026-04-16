from database.conexao import conectar

def inserir_usuario(usuario, senha):
    """Função que cadastra o usuário"""

    try:
        conexao, cursor = conectar()
        cursor.execute("INSERT INTO tb_usuario (usuario, senha) VALUES (%s, %s);", (usuario, senha))
        conexao.commit()
        conexao.close()
        return True
    
    except Exception as erro:
        print(erro)
        return False
    
def verificar_login(usuario, senha):
    """Função que verifica se o usuário está cadastrado"""

    conexao, cursor = conectar()
    cursor.execute("SELECT usuario, senha FROM tb_usuario WHERE usuario = %s AND senha = %s;", (usuario, senha))
    user = cursor.fetchone()
    conexao.close()
    return user