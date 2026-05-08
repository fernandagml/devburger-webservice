from database.conexao import conectar

def recuperar_produto_carrinho(usuario:str) -> list:
    """Função criada para buscar os produtos no carrinho de um determinado usuário."""

    conexao, cursor = conectar()
    cursor.execute("""
    SELECT tb_carrinho.id_carrinho, tb_itens_carrinho.quantidade, tb_carrinho.usuario, tb_carrinho.finalizado, tb_carrinho.data_carrinho, tb_produto.preco, tb_produto.nome_produto, tb_produto.imagem
    FROM tb_itens_carrinho
    INNER JOIN tb_produto ON tb_produto.id_produto = tb_itens_carrinho.id_produto
    INNER JOIN tb_carrinho ON tb_carrinho.id_carrinho = tb_itens_carrinho.id_carrinho
    WHERE tb_carrinho.usuario = %s;""", (usuario, ))
    produtos_carrinho = cursor.fetchall()
    conexao.close()
    return produtos_carrinho

def inserir_item_usuario(usuario, id_produto, quantidade=1):
    conexao, cursor = conectar()
    cursor.execute("""SELECT id_carrinho FROM tb_carrinho WHERE usuario = %s AND finalizado = 0 LIMIT 1;""", (usuario, ))
    carrinho = cursor.fetchone()
    if carrinho:
        id_carrinho = carrinho["id_carrinho"]
    else:
        cursor.execute("""INSERT INTO tb_carrinho (usuario) VALUE (%s)""", (usuario, ))
        id_carrinho = cursor.lastrowid
    cursor.execute("""INSERT INTO tb_itens_carrinho (id_carrinho, id_produto, quantidade) VALUES (%s, %s, %s)""", (id_carrinho, id_produto, quantidade))
    conexao.commit()
    conexao.close()

def delete_item_usuario(id_produto):
    conexao, cursor = conectar()
    cursor.execute("""DELETE FROM tb_itens_carrrinho WHERE id_produto = %s;""", (id_produto, ))
    conexao.commit()
    conexao.close()