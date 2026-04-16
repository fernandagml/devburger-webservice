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
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(80),
    senha VARCHAR(200)
);