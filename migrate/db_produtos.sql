create database if not exists produto;
use produto;

CREATE table IF NOT EXISTS itens(
codigo int NOT NULL PRIMARY KEY auto_increment,
produto varchar(50),
descricao varchar(50),
destaque bool,
valor float,
imagem varchar(300),
disponibilidade bool
);

CREATE table if not exists login(
codigo int not null primary key auto_increment,
nome varchar (50),
usuario varchar (50),
senha varchar(200)
);

CREATE table if not exists carrinho(
cod_carrinho int auto_increment primary key,
usuario varchar(50),
data datetime default current_timestamp,
finalizado bool,
CONSTRAINT fk_carrinho_login FOREIGN KEY (usuario) REFERENCES  login(usuario)
);

CREATE table if not exists item_carrinho(
cod_item_carrinho int auto_increment primary key,
cod_carrinho int,
cod_itens int, 
quantidade int default 1,
CONSTRAINT fk_itemcarrinho_carrinho FOREIGN KEY (cod_carrinho) REFERENCES carrinho(cod_carrinho),
CONSTRAINT fk_itemcarrinho_itens FOREIGN KEY(cod_produto) REFERENCES itens(codigo)
);