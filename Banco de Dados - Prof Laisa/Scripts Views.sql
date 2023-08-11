select * from avaliacao
select * from categoria
select * from cliente
select * from pedido
	where id_cliente = 2
select * from pedido_produtos
join pedido
	on pedido.id_pedido = pedido_produtos.id_pedido
where pedido.data_pedido > '2022-12-31' and pedido.data_pedido < '2023-04-01' and pedido_produtos.quantidade < 2

limit 30
select * from produto

select * from produto
join categoria
on produto.id_categoria = categoria.id_categoria

create view pedidos_feitos_por_clientes as

select * from cliente

select cliente.nome as "cliente", pedido.id_pedido as "IDpedido", pedido.valor_total as "ValorPedido",
pedido_produtos.valor as "ValorProduto", pedido_produtos.quantidade as "qntDoProduto", produto.nome as "NomeProduto"  from cliente
left join pedido
	on cliente.id_cliente = pedido.id_cliente
join pedido_produtos
	on pedido.id_pedido = pedido_produtos.id_pedido
join produto
	on pedido_produtos.id_produto = produto.id_produto
order by cliente.nome
limit 15


select * from produtos_vendido

create view produtos_menos_vendidos_no_brasil_1trimestre_2023 as


select max(pedido_produtos.quantidade) as "QntMaxVendida", cliente.country as "PaísDoPedido" from produto
left join pedido_produtos
	on produto.id_produto = pedido_produtos.id_produto
left join pedido
	on pedido_produtos.id_pedido = pedido.id_pedido
left join cliente
	on pedido.id_cliente = cliente.id_cliente
where cliente.country = 'Brasil' and pedido.data_pedido > '2022-12-31' and pedido.data_pedido < '2023-04-01' and pedido_produtos.quantidade < 8
group by cliente.country, pedido.data_pedido
limit 30



select data_pedido,pedido.id_cliente,pedido.id_pedido,produto.id_produto,pedido_produtos.quantidade as "QntMaxVendida", cliente.country as "PaísDoPedido" from produto
left join pedido_produtos
	on produto.id_produto = pedido_produtos.id_produto
left join pedido
	on pedido_produtos.id_pedido = pedido.id_pedido
left join cliente
	on pedido.id_cliente = cliente.id_cliente
where cliente.country = 'Brasil' and pedido.data_pedido > '2022-12-31' and pedido.data_pedido < '2023-04-01' and pedido_produtos.quantidade < 2
limit 30




















select * from produtos_menos_vendidos

create view menos_vendidos_2semestre2023_e_menor_que_10reais as
select cliente.nome as "Cliente", pedido.id_pedido as "IDpedido", pedido.data_pedido as "Data", count(pedido_produtos.valor) as "Quantidade",
produto.nome as "NomeDoProduto", produto.valor as "Valor" from cliente
left join pedido
	on cliente.id_cliente = pedido.id_cliente
join pedido_produtos
	on pedido.id_pedido = pedido_produtos.id_pedido
join produto
	on pedido_produtos.id_produto = produto.id_produto
where pedido.data_pedido > '2023-07-01' and pedido_produtos.valor is not null and produto.valor < 10
group by cliente.nome, pedido.id_pedido, pedido_produtos.valor, produto.nome, produto.valor
limit 15



create view maior_nota_br_fr as
select max(avaliacao.nota) as "Nota", cliente.nome as "NomeDoCliente",
cliente.country as "PaísDeOrigem" from avaliacao
left join produto
	on produto.id_produto = avaliacao.id_produto
join pedido_produtos
	on produto.id_produto = pedido_produtos.id_produto
join cliente
	on avaliacao.id_cliente = cliente.id_cliente
join pedido
	on pedido.id_pedido = pedido_produtos.id_pedido
	and pedido.id_cliente = cliente.id_cliente
where (cliente.country like 'Brasil' or cliente.country like 'França') and avaliacao.nota >= 1 and pedido.valor_total > 10
group by cliente.nome, cliente.country
limit 15

insert into avaliacao(comentario, nota, id_produto, id_cliente) values('Muinto boua a agua cadura', '9', '3', '2')
insert into pedido(data_pedido, valor_total, id_cliente) values('2022-12-15', '20.37', '2')
insert into pedido_produtos(valor, quantidade, id_produto, id_pedido) values('20.37', '3', '3', '7')

select * from preco_min
select * from pedidos_feitos_por_clientes
select * from produtos_menos_vendidos
select * from produtos_vendido
select * from produtos_mais_vendidos

select * from maior_nota_br_fr
select * from produtos_menos_vendidos_no_brasil_1trimestre_2023
select * from menos_vendidos_2semestre2023_e_menor_que_10reais