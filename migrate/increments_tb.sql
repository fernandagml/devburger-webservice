INSERT INTO tb_produto (nome_produto, descricao, preco, imagem, destaque, estoque) 
VALUES
('Classic Dev', 'Pão brioche, carne suculenta de 160g e queijo cheddar derretido.', 25.00, 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600', 0, 1),
('Double Stack', 'Dois hambúrgueres, bacon crocante e molho especial.', 38.00, 'https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=600', 1, 1),
('Veggie Script', 'Hambúrguer de grão de bico com salada fresca.', 30.00, 'https://images.pexels.com/photos/3219483/pexels-photo-3219483.jpeg?auto=compress&cs=tinysrgb&w=600', 1, 1),
('Java Chicken', 'Frango empanado crocante com alface e maionese.', 28.00, 'https://images.pexels.com/photos/12034622/pexels-photo-12034622.jpeg', 0, 1),
('Python Onion', 'Anéis de cebola, barbecue e queijo cheddar.', 33.00, 'https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg?auto=compress&cs=tinysrgb&w=600', 1, 1),
('React Salad', 'Uma opção leve e reativa para o seu almoço.', 27.00, 'https://images.pexels.com/photos/1199957/pexels-photo-1199957.jpeg?auto=compress&cs=tinysrgb&w=600', 0, 1);

INSERT INTO `db_devburguer`.`tb_carrinho` (`finalizado`, `usuario`) VALUES ('0', 'Fer');

INSERT INTO `db_devburguer`.`tb_itens_carrinho` (`quantidade`, `id_carrinho`, `id_produto`) VALUES ('2', '1', '3');
INSERT INTO `db_devburguer`.`tb_itens_carrinho` (`quantidade`, `id_carrinho`, `id_produto`) VALUES ('4', '1', '5');

SELECT tb_carrinho.id_carrinho, tb_itens_carrinho.quantidade, tb_carrinho.usuario, tb_carrinho.finalizado, tb_carrinho.data_carrinho, tb_produto.preco
FROM tb_itens_carrinho
INNER JOIN tb_produto ON tb_produto.id_produto = tb_itens_carrinho.id_produto
INNER JOIN tb_carrinho ON tb_carrinho.id_carrinho = tb_itens_carrinho.id_carrinho
WHERE usuario = "Fer";