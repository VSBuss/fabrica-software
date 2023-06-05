CREATE TABLE CARRO(
ID_CARRO SERIAL PRIMARY KEY,
MARCA VARCHAR(30) NOT NULL,
MODELO VARCHAR(30) NOT NULL,
ANO INT NOT NULL
);

CREATE TABLE ALUGUEIS(
ID_ALUGUEL SERIAL PRIMARY KEY,
DIAS_ALUGUEL INT NOT NULL, 
ID_CARRO INT NOT NULL,
ID_CLIENTE INT NOT NULL
);

CREATE TABLE CLIENTE(
ID_CLIENTE SERIAL PRIMARY KEY,
NOME VARCHAR(50) NOT NULL
);

INSERT INTO CLIENTE(NOME) VALUES('Francisco');
INSERT INTO CLIENTE(NOME) VALUES('Rogério');
INSERT INTO CLIENTE(NOME) VALUES('Andressa');
INSERT INTO CLIENTE(NOME) VALUES('Joana');
INSERT INTO CLIENTE(NOME) VALUES('Carlos');
INSERT INTO CLIENTE(NOME) VALUES('Henrique');
INSERT INTO CLIENTE(NOME) VALUES('Patrícia');
INSERT INTO CLIENTE(NOME) VALUES('Pedro');
INSERT INTO CLIENTE(NOME) VALUES('Luisa');
INSERT INTO CLIENTE(NOME) VALUES('Maria');
INSERT INTO CLIENTE(NOME) VALUES('Jorge');
INSERT INTO CLIENTE(NOME) VALUES('Luana');

INSERT INTO CARRO(MARCA, MODELO, ANO) VALUES('Hyundai', 'HB20', '2022');
INSERT INTO CARRO(MARCA, MODELO, ANO) VALUES('Chevrolet', 'Onix', '2018');
INSERT INTO CARRO(MARCA, MODELO, ANO) VALUES('Fiat', 'Mobi', '2021');
INSERT INTO CARRO(MARCA, MODELO, ANO) VALUES('Volkswagen', 'Gol', '2022');
INSERT INTO CARRO(MARCA, MODELO, ANO) VALUES('Fiat', 'Argo', '2020');
INSERT INTO CARRO(MARCA, MODELO, ANO) VALUES('Renault', 'Kwid', '2021');

/*THAT'S HOW YOU REFERENCE A FOREIGN KEY AFTER CREATING A TABLE*/
ALTER TABLE ALUGUEIS ADD CONSTRAINT ID_CARRO FOREIGN KEY(ID_CARRO) REFERENCES CARRO(ID_CARRO);
ALTER TABLE ALUGUEIS ADD CONSTRAINT ID_CLIENTE FOREIGN KEY(ID_CLIENTE) REFERENCES CLIENTE(ID_CLIENTE);

INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('3', '1', '4');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('5', '3', '5');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('7', '5', '8');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('2', '1', '10');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('15', '2', '8');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('22', '4', '1');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('44', '6', '11');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('16', '3', '12');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('14', '1', '4');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('14', '5', '9');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('7', '5', '2');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('3', '2', '12');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('10', '1', '5');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('14', '5', '6');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('32', '6', '2');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('27', '3', '11');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('20', '4', '3');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('9', '2', '9');
INSERT INTO ALUGUEIS(DIAS_ALUGUEL, ID_CARRO, ID_CLIENTE) VALUES('12', '1', '7');

SELECT * FROM ALUGUEIS



SELECT ID_ALUGUEL, DIAS_ALUGUEL, CLIENTE.NOME, CARRO.MARCA, CARRO.MODELO, CARRO.ANO
FROM ALUGUEIS
	JOIN CLIENTE
		ON CLIENTE.ID_CLIENTE = ALUGUEIS.ID_CLIENTE
	JOIN CARRO
		ON CARRO.ID_CARRO = ALUGUEIS.ID_CARRO
GROUP BY ALUGUEIS.ID_CLIENTE, ALUGUEIS.ID_ALUGUEL, CLIENTE.ID_CLIENTE, CARRO.ID_CARRO
ORDER BY ID_ALUGUEL



SELECT MARCA, MODELO, ANO, COUNT(ALUGUEIS.ID_CARRO) AS QNTALUGADO
FROM CARRO
	JOIN ALUGUEIS
		ON ALUGUEIS.ID_CARRO = CARRO.ID_CARRO
GROUP BY ALUGUEIS.ID_CARRO, MARCA, MODELO, ANO



SELECT NOME, SUM(ALUGUEIS.DIAS_ALUGUEL) AS DURACAOTOTAL
FROM CLIENTE
	JOIN ALUGUEIS
		ON ALUGUEIS.ID_CLIENTE = CLIENTE.ID_CLIENTE
GROUP BY CLIENTE.NOME
ORDER BY NOME



SELECT MARCA, AVG(ALUGUEIS.DIAS_ALUGUEL)
FROM CARRO
	JOIN ALUGUEIS
		ON ALUGUEIS.ID_CARRO = CARRO.ID_CARRO
GROUP BY MARCA