CREATE TABLE Avaliacao(
ID_AVALIACAO SERIAL PRIMARY KEY,
COMENTARIO VARCHAR(255) NOT NULL,
NOTA INT NOT NULL,
ID_PRODUTO INT NOT NULL,
ID_CLIENTE INT NOT NULL,
FOREIGN KEY (ID_PRODUTO) REFERENCES Produto (ID_PRODUTO),
FOREIGN KEY (ID_CLIENTE) REFERENCES Cliente (ID_CLIENTE)
);

CREATE TABLE Cliente(
ID_CLIENTE SERIAL PRIMARY KEY,
NOME VARCHAR(200) NOT NULL,
CPF VARCHAR(11) NOT NULL,
EMAIL VARCHAR(100) NOT NULL
);

CREATE TABLE Categoria(
ID_CATEGORIA SERIAL PRIMARY KEY,
NOME VARCHAR(100) NOT NULL
);

CREATE TABLE Produto(
ID_PRODUTO SERIAL PRIMARY KEY,
NOME VARCHAR(200) NOT NULL,
VALOR FLOAT NOT NULL,
ID_CATEGORIA INT NOT NULL,
FOREIGN KEY (ID_CATEGORIA) REFERENCES Categoria (ID_CATEGORIA)
);

CREATE TABLE Pedido_Produtos(
ID_PEDIDO_PRODUTOS SERIAL PRIMARY KEY,
VALOR FLOAT NOT NULL,
QUANTIDADE INT NOT NULL,
ID_PRODUTO INT NOT NULL,
ID_PEDIDO INT NOT NULL,
FOREIGN KEY (ID_PRODUTO) REFERENCES Produto (ID_PRODUTO),
FOREIGN KEY (ID_PEDIDO) REFERENCES Pedido (ID_PEDIDO)
);

CREATE TABLE Pedido(
ID_PEDIDO SERIAL PRIMARY KEY,
DATA_PEDIDO DATE NOT NULL,
VALOR_TOTAL FLOAT NOT NULL,
ID_CLIENTE INT NOT NULL,
FOREIGN KEY (ID_CLIENTE) REFERENCES Cliente (ID_CLIENTE)
);

INSERT INTO Categoria(nome) VALUES ('Eletrônicos');
INSERT INTO Categoria(nome) VALUES ('Móveis');
INSERT INTO Categoria(nome) VALUES ('Limpeza');
INSERT INTO Categoria(nome) VALUES ('Pet');
INSERT INTO Categoria(nome) VALUES ('Livros');

INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Telefone','849.89','1');
INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Fone de Ouvido','19.99','1');
INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Água Sanitária','6.79','3');
INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Escova de Dentes','12.49','3');
INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Sofá 3 lugares','1969.99','2');
INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Harry Potter A Ameaça de Dobby','9.34','5');
INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Cadeira','98.98','2');
INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Cartas de um Anjo a Seu Aprendiz','7.11','5');
INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Galinha de plástico','9.99','4');
INSERT INTO Produto(nome, valor, id_categoria) VALUES ('Ração vegana sabor peixe','149.99','4');

INSERT INTO Cliente(NOME, CPF_CLIENTE, EMAIL) VALUES ('André Augusto Parse','183.456.789-99','andre_guto@seninha.com.br');
INSERT INTO Cliente(NOME, CPF_CLIENTE, EMAIL) VALUES ('Luiza Liz Lais','999.999.999-99','lu.fafa99@ibest.com.br');
INSERT INTO Cliente(NOME, CPF_CLIENTE, EMAIL) VALUES ('Brendon Larisso Antoniel','789.456.123-22','priest_br@uol.com.br');
INSERT INTO Cliente(NOME, CPF_CLIENTE, EMAIL) VALUES ('Pedro Borgonha','321.987.654-49','pegonha77@iguinho.com.br');

SELECT * FROM Pedido_PRODUTOS

ALTER TABLE Cliente
RENAME COLUMN CPF TO CPF_CLIENTE;

ALTER TABLE Cliente
ALTER COLUMN CPF_CLIENTE TYPE VARCHAR(14);

/*Usado para selecionar todas as tabelas*/
SELECT * FROM pg_tables
/*Junto com o código logo acima seleciona todas as tabelas com o valor schemaname 'public' */
WHERE schemaname = 'public'

INSERT INTO Avaliacao(COMENTARIO, NOTA, ID_PRODUTO, ID_CLIENTE) VALUES ('Muito ruin ocelular, finca travano', '2', '1', '2');
INSERT INTO Avaliacao(COMENTARIO, NOTA, ID_PRODUTO, ID_CLIENTE) VALUES ('Faz muito barulho, gostei bastante. Consigo me divertir demais com o meu cachorrinho.', '10', '9', '1');
INSERT INTO Avaliacao(COMENTARIO, NOTA, ID_PRODUTO, ID_CLIENTE) VALUES ('Não comprem esse fone de ouvido. Já é a terceira vez que eu vejo reclamação de eletrônicos dessa loja, nunca mais compro aqui.', '1', '2', '4');
INSERT INTO Avaliacao(COMENTARIO, NOTA, ID_PRODUTO, ID_CLIENTE) VALUES ('Muito bom o livro, só não dou nota 10 porque nota máxima só a Bíblia. Amém?', '9', '6', '3');



INSERT INTO Pedido(data_pedido, valor_total, ID_CLIENTE) VALUES ('06/09/2023', '16.45', '3');
INSERT INTO Pedido(data_pedido, valor_total, ID_CLIENTE) VALUES ('28/02/2023', '179.26', '1');
INSERT INTO Pedido(data_pedido, valor_total, ID_CLIENTE) VALUES ('16/01/2023', '849.89', '2');
INSERT INTO Pedido(data_pedido, valor_total, ID_CLIENTE) VALUES ('25/05/2023', '2425.88', '4');



INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('849.89', '1', '1', '3');
/*REGISTROS ERRADOS*/
INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('149.99', '1', '10', '2');
INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('9.99', '1', '9', '3');
INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('6.79', '1', '3', '3');
INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('12.49', '1', '4', '3');

INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('395.92', '4', '7', '4');
INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('1969.99', '1', '5', '4');
INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('59.97', '3', '2', '4');

INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('9.34', '1', '6', '1');
INSERT INTO Pedido_Produtos(valor, quantidade, ID_PRODUTO, ID_PEDIDO) VALUES ('7.11', '1', '8', '1');

SELECT CLIENTE.ID_CLIENTE AS CODIGO_CLIENTE, CLIENTE.NOME, DATA_PEDIDO AS DATADOPEDIDO, VALOR_TOTAL, PEDIDO.ID_PEDIDO, PRODUTO.NOME FROM CLIENTE
LEFT JOIN PEDIDO
ON CLIENTE.ID_CLIENTE = PEDIDO.ID_CLIENTE
LEFT JOIN PEDIDO_PRODUTOS
ON PEDIDO.ID_PEDIDO = PEDIDO_PRODUTOS.ID_PEDIDO
LEFT JOIN PRODUTO
ON PEDIDO_PRODUTOS.ID_PRODUTO = PRODUTO.ID_PRODUTO
ORDER BY CODIGO_CLIENTE

SELECT CLIENTE.ID_CLIENTE, NOME, NOTA, COMENTARIO FROM CLIENTE
JOIN AVALIACAO
ON CLIENTE.ID_CLIENTE = AVALIACAO.ID_CLIENTE
WHERE NOTA < 3
ORDER BY NOTA

/*DELETA REGISTRO DE TABELA COM BASE NO VALOR DO ID*/
DELETE FROM PEDIDO_PRODUTOS
WHERE ID_PEDIDO_PRODUTOS IN (17, 18, 19)

/*TROCA VALOR DE ID_PEDIDO DE REGISTROS EM PEDIDO_PRODUTOS*/
UPDATE PEDIDO_PRODUTOS
SET ID_PEDIDO = 2
WHERE ID_PEDIDO_PRODUTOS IN (9, 10, 11)