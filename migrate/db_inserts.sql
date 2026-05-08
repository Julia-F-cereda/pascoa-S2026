USE produto;
INSERT INTO `produto`.`itens`
(
produto, 
descricao, 
destaque, 
valor, 
imagem, 
disponibilidade
)
VALUES(
"X-TUDO",
"Compra que é top",
"1",
"40.00",
"https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=200",
"1"
),

("X-TO",
"Compra que é top",
"0",
"40.00",
"https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=200",
"1"
),

("X-SALADA",
"Compra que é top",
"1",
"40.00",
"https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=200",
"1"
);

INSERT INTO `produto`.`login`
(nome,
usuario,
senha)
VALUES
('Godofredo', 
'123',
'Godo Frede');



insert into produto.item_carrinho
cod_item_carrinho, cod_carrinho, cod_itens, quantidade

INSERT INTO `produto`.`carrinho`
(cod_usuario,
finalizado)
VALUES
('1',
'1')

INSERT INTO `produto`.`item_carrinho`
(cod_carrinho,
 cod_itens,
 quantidade)
 VALUES
 ('1',
 '1',
 '1');