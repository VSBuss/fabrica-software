class Produto
{
    constructor()
    {
        this.id=1;
        this.arrayProdutos=[];
    }

    validarCampos(produto)
    {
        let msg = '';
        if(produto.nomeProduto == '')
        {
            msg += 'Coloca o nome do produto, gajo. ';
        }
        if(produto.preco == '')
        {
            msg += 'Sumiste com o preço do produto? Quer me falir?';
        }
        if(msg != '')
        {
            alert(msg);
            return false;
        }

        return true
    }

    cancelar(){

    }


    adicionar(produto)
    {
        this.arrayProdutos.push(produto);
        this.id ++;
    }

    lerDados()
    {
        let produto = {};

        produto.id = this.id;
        produto.nomeProduto = document.getElementById('produto').value;
        produto.preco = document.getElementById('preco').value;

        return produto;
    }

    listarTabela()
    {
        let tbody = document.getElementById('tbody');
        tbody.innerText = '';

        for (let i=0;i<this.arrayProdutos.length;i++)
        {
            let tr = tbody.insertRow();

            let td_id = tr.insertCell();
            let td_produto = tr.insertCell();
            let td_valor = tr.insertCell();

            td_id.innerText = this.arrayProdutos[i].id;
            td_produto.innerText = this.arrayProdutos[i].nomeProduto;
            td_valor.innerText = this.arrayProdutos[i].preco;

        }
    }

    salvar()
    {
        let produto = this.lerDados();
        if(this.validarCampos(produto))
        {
            this.adicionar(produto);
        }

        this.listarTabela();
    }
}

var produto = new Produto();