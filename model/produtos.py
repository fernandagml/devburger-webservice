from database.conexao import conectar

def recuperar_produtos(estoque):
    """Função criada para buscar os produtos no banco de dados."""

    conexao, cursor = conectar()
    cursor.execute("SELECT id_produto, nome_produto, preco, descricao, imagem, destaque, estoque FROM tb_produto WHERE estoque = 1;")
    produtos = cursor.fetchall()
    conexao.close()
    return produtos