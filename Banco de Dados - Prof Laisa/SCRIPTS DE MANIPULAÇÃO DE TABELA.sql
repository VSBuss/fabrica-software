--Insere os registros na tabela 'usuario' (Usar sempre aspas simples)--
INSERT INTO usuario(nome_user, cpf, cep, telefone) VALUES ('Axelandre Refeira','980.765.358-33','78635-78','67989771212');

--Código abaixo seleciona todos os registros da tabela 'livro' e o visualiza--
SELECT * from livro

--Código abaixo seleciona apenas os registros 'cpf' e 'cep' da tabela 'usuario'--
SELECT cpf, cep from usuario

--Altera a tabela 'livro'--
ALTER TABLE livro
--Abaixo insere a coluna 'id_editor' na tabela 'livro' e indica o tipo de dado como 'INT'--
ADD COLUMN id_editor INT

--Código abaixo seleciona a tabela 'livro' para edição--
UPDATE livro
-->SET< insere o valor '3' na coluna/registro 'id_editor' e >WHERE< indica a linha com base no 'id_livro'--
SET id_editor = 3
WHERE id_livro = 2
--Código abaixo seleciona a tabela 'editor' e >JOIN< junta a tabela 'editor' com a tabela 'livro'--
SELECT * FROM editor
JOIN LIVRO
ON EDITOR.ID_EDITOR = LIVRO.ID_EDITOR