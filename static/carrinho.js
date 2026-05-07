async function mostrar_carrinho()
{
    const resposta = await fetch("http://127.0.0.1:5000/api/get/carrinho")
  
    if (!resposta.ok){
    }
    else{
        const dados = await resposta.json()
        const carrinho = document.getElementById("produtos")
        carrinho.innerHTML = "";
        let total = 0;

        for (let dado of dados){
            total += dado.preco
            let linha = `

            <div class="produto">
                <span>${dado.nome}</span>
                <span>${dado.preco}</span>
            </div>
`
        carrinho.innerHTML += linha
        }
    }
}

mostrar_carrinho()

async function inserirItemCarrinho(cod_itens, quantidade=1) {
    const resposta = await fetch("/api/post/item_carrinho", 
                                            {
                                            method: "POST", 
                                            headers:{
                                            "Content-Type": "application/json"
                                                    }, 
                                            body: JSON.stringify(
                                            {
                                                    "cod_itens": cod_itens,
                                                    "quantidade": quantidade,
                                            }
                                            )
                                        }
                                    )

    if (!resposta.OK)
    {
        alert("erro ao inserir item")
    }
    mostrar_carrinho();
}
    