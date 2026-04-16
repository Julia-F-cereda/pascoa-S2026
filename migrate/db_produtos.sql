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
)

CREATE table if not exists login(
codigo int not null primary key auto_increment,
usuario varchar (50),
senha varchar(200)
);
