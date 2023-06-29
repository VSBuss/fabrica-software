select * from avaliacao
select * from categoria
select * from cliente
select * from pedido
select * from pedido_produtos
select * from produto

select * from produto
join categoria
on produto.id_categoria = categoria.id_categoria

create view pedidos_feitos_por_clientes as
select * from cliente
select cliente.nome as "cliente", pedido.id_pedido as "IDpedido", pedido_produtos.valor as "ValorPedido", pedido_produtos.valor as "ValorProduto", pedido_produtos.quantidade as "qntDoProduto", produto.nome as "NomeProduto"  from cliente
left join pedido
	on cliente.id_cliente = pedido.id_cliente
join pedido_produtos
	on pedido.id_pedido = pedido_produtos.id_pedido
join produto
	on pedido_produtos.id_produto = produto.id_produto
where pedido_produtos.quantidade > 1
limit 15

select * from preco_min
select * from pedidos_feitos_por_clientes