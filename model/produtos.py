from database.conexao import conectar

def recuperar_produtos():
    """Função criada para buscar os produtos no banco de dados."""

    conexao, cursor = conectar()
    cursor.execute("SELECT id_produto, nome_produto, preco, descricao, imagem, destaque, estoque FROM tb_produto WHERE estoque = 1;")
    produtos = cursor.fetchall()
    conexao.close()
    return produtos

def recuperar_produto_id(id):

    conexao, cursor = conectar()
    cursor.execute("SELECT id_produto, nome_produto, preco, descricao, imagem, destaque, estoque FROM tb_produto WHERE id_produto = %s;", (id, ))
    produto = cursor.fetchone()
    conexao.close()
    return produto

def recuperar_produto_destaque():

    conexao, cursor = conectar()
    cursor.execute("SELECT id_produto, nome_produto, preco, descricao, imagem, destaque, estoque FROM tb_produto WHERE destaque = 1;")
    destaque = cursor.fetchall()
    conexao.close()
    return destaque