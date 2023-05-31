select * from cliente
select * from avaliacao
select * from produto
select * from pedido
select * from pedido_produtos

/*Insere a coluna 'country' na tabela cliente*/
alter table cliente
add column country varchar(20);

/*Insere registros novos dentro da tabela cliente*/
update cliente
set country = 'Argentina'
where id_cliente = 1;

update cliente
set country = 'Brasil'
where id_cliente = 2;

update cliente
set country = 'Itália'
where id_cliente = 3;

update cliente
set country = 'França'
where id_cliente = 4;

update cliente
set nome = 'Jaques Ferreira Junior', cpf_cliente = '420.069.171-52', email = 'jaquesfjr@kpoper.com', country = 'Guiana Francesa'
where id_cliente = 5;

insert into cliente (nome, cpf_cliente, email, country) values ('Manuela de la Muerte', '567.266.379-51', 'lamuerta@limbo.net', 'Argentina');
insert into cliente (nome, cpf_cliente, email, country) values ('Borges Ludo Marques Perron', '967.276.339-18', 'borludomarquesperron@indpbre.net', 'Paraguai');
insert into avaliacao (comentario, nota, id_produto, id_cliente) values ('No tiene otro sabor', '6', '10', '7');
insert into pedido (data_pedido, valor_total, id_cliente) values ('2023-02-17', '149.99', '7');
insert into pedido_produtos (valor, quantidade, id_produto, id_pedido) values ('149.99', '1', '10', '5');
insert into pedido (data_pedido, valor_total, id_cliente) values ('2023-01-05', '565.9', '3');
insert into pedido_produtos (valor, quantidade, id_produto, id_pedido) values ('19.99', '1', '2', '6');
insert into pedido_produtos (valor, quantidade, id_produto, id_pedido) values ('395.92', '4', '7', '6');
insert into pedido_produtos (valor, quantidade, id_produto, id_pedido) values ('149.99', '1', '10', '6');

/*CALCULAR O TOTAL DE PEDIDOS REALIZADOS POR CADA CLIENTE*/
SELECT PEDIDO.ID_CLIENTE,
	CLIENTE.NOME,
	COUNT(PEDIDO.ID_CLIENTE) AS PEDIDOSDOCLIENTE
FROM PEDIDO
	RIGHT JOIN CLIENTE
		ON PEDIDO.ID_CLIENTE = CLIENTE.ID_CLIENTE
GROUP BY PEDIDO.ID_CLIENTE, CLIENTE.NOME
ORDER BY PEDIDO.ID_CLIENTE

/*CALCULAR A RECEITA TOTAL DE CADA PAÍS, SOMANDO O VALOR DOS PEDIDOS*/
SELECT CLIENTE.COUNTRY AS PAISES,
	SUM(PEDIDO.VALOR_TOTAL) AS SOMAPORPEDIDO
FROM PEDIDO
	JOIN CLIENTE
		ON PEDIDO.ID_CLIENTE = CLIENTE.ID_CLIENTE
GROUP BY CLIENTE.COUNTRY
ORDER BY CLIENTE.COUNTRY