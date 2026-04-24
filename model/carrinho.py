from database.conexao import conectar

def recuperar_produto_carrinho(usuario:str) -> list:
    """Função criada para buscar os produtos no carrinho de um determinado usuário."""

    conexao, cursor = conectar()
    cursor.execute("""
    SELECT tb_carrinho.id_carrinho, tb_itens_carrinho.quantidade, tb_carrinho.usuario, tb_carrinho.finalizado, tb_carrinho.data_carrinho, tb_produto.preco
    FROM tb_itens_carrinho
    INNER JOIN tb_produto ON tb_produto.id_produto = tb_itens_carrinho.id_produto
    INNER JOIN tb_carrinho ON tb_carrinho.id_carrinho = tb_itens_carrinho.id_carrinho
    WHERE tb_carrinho.usuario = "Fer";""", (usuario, ))
    produtos_carrinho = cursor.fetchall()
    conexao.close()
    return produtos_carrinho