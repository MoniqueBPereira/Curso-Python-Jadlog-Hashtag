if OBJECT_ID('vwFatoVendas', 'V') is not null
    drop view vwFatoVendas

exec('
    create view vwFatoVendas as
    select 
        pedidos.idPedido,
        pedidos.dataPedido,
        clientes.nomeCliente,
        vendedores.nomeVendedor,
        regionais.nomeRegional,
        produtos.nomeProduto,
        linhasProdutos.nomeLinhaProduto,
        itensPedido.quantidade,
        itensPedido.precoUnitario,
        (itensPedido, quantidade * (itensPedido.precoUnitario - itensPedido.desconto)) as valor_total
        
        from pedidos
        join clientes on pedidos.fkCliente = clientes.idPedido
        join vendedores on pedidos.fkVendedor = vendedores.idVendedor
        join regionais on vendedores.fkRegional = regionais.idRegional
        join itensPedido on itensPedido.fkPedido = pedidos.idPedido
        join produtos on itensPedido.fkProduto = produtos.idProduto
        join linhasProdutos on produtos.fkLinhaProduto = linhasProdutos.idLinhaProduto
')