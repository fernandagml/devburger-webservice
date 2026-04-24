CREATE DATABASE IF NOT EXISTS db_devburguer;
USE db_devburguer;

CREATE TABLE IF NOT EXISTS tb_produto (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(100) NOT NULL,
    descricao VARCHAR(200),
    preco REAL NOT NULL,
    imagem VARCHAR(255),
    destaque BOOL,
    estoque BOOL
);

CREATE TABLE IF NOT EXISTS tb_usuario (
    usuario VARCHAR(80) PRIMARY KEY,
    senha VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_carrinho (
	id_carrinho INT PRIMARY KEY AUTO_INCREMENT,
    data_carrinho DATETIME DEFAULT CURRENT_TIMESTAMP,
    finalizado BOOL,
    usuario VARCHAR(80),
    CONSTRAINT FK_usuario_carrinho
    FOREIGN KEY (usuario)
    REFERENCES tb_usuario(usuario)
);

CREATE TABLE IF NOT EXISTS tb_itens_carrinho (
	quantidade INT,
    id_carrinho INT,
	id_produto INT,
    CONSTRAINT FK_produto_itens
    FOREIGN KEY (id_produto)
    REFERENCES tb_produto(id_produto),
    CONSTRAINT FK_carrinho_itens
    FOREIGN KEY (id_carrinho)
    REFERENCES tb_caRrinho(id_carrinho),
    PRIMARY KEY (id_carrinho, id_produto)
);