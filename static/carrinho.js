async function mostrar_carrinho()
{
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")
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