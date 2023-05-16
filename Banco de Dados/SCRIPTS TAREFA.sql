CREATE TABLE cliente(
id_cliente SERIAL PRIMARY KEY,
nome_cliente VARCHAR(50) NOT NULL,
cpf VARCHAR(14) NOT NULL,
cep VARCHAR(8) NOT NULL,
telefone VARCHAR(11) NOT NULL
);

CREATE TABLE produto(
id_produto SERIAL PRIMARY KEY,
nome_produto VARCHAR(50) NOT NULL,
valor_produto FLOAT NOT NULL,
estoque INT NOT NULL
);

CREATE TABLE venda(
id_venda SERIAL PRIMARY KEY,
datacompra DATE NOT NULL,
nf INT NOT NULL,
id_cliente INT NOT NULL,
id_pedido INT NOT NULL
);

CREATE TABLE pedido(
id_pedido SERIAL PRIMARY KEY,
id_cliente INT NOT NULL,
id_produto INT NOT NULL
);