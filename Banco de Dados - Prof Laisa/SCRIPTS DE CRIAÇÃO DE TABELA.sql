CREATE TABLE usuario(
id_user SERIAL PRIMARY KEY,
nome_user VARCHAR(50) NOT NULL,
cpf VARCHAR(14) NOT NULL,
cep VARCHAR(8) NOT NULL,
telefone VARCHAR(11) NOT NULL
);

CREATE TABLE editor(
id_editor SERIAL PRIMARY KEY,
nome_editor VARCHAR(50) NOT NULL
);

CREATE TABLE emprestimo(
id_emprestimo SERIAL PRIMARY KEY,
data_retirada DATE NOT NULL,
data_entrega DATE
);

CREATE TABLE livro(
id_livro SERIAL PRIMARY KEY,
nome_livro VARCHAR(50) NOT NULL,
genero VARCHAR(20) NOT NULL,
idioma VARCHAR(20) NOT NULL,
qnt_livros INT NOT NULL,
ano_publi INT
);

CREATE TABLE autor(
id_autor SERIAL PRIMARY KEY,
nome_autor VARCHAR(50),
nacionalidade VARCHAR(20)
);