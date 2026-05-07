async function mostrarCarrinho() {
    const resposta = await fetch("/api/get/carrinho")

    if (!resposta.ok) {
        alert("Erro ao carregar!")
    } else {
        const dados = await resposta.json()
        const carrinho = document.getElementById('carrinho')
        carrinho.innerHTML = "";

        let total = 0;

        for (let dado of dados) {

            total = total + dado.preco

            let linha = `
            <div class="carrinho-conteudo" id="carrinho">
                <div class="item-carrinho">
                    <div class="container-img">
                        <img src="${dado.imagem}" alt="${dado.nome_produto}" class="item-imagem">
                    </div>
                    <div class="item-info">
                        <span class="item-nome">${dado.nome_produto}</span>
                        <span class="item-quantidade">${dado.quantidade} <em>un.</em></span>
                        <span class="item-preco">R$ ${dado.preco}</span>
                    </div>
                </div>
            </div>
            `
            carrinho.innerHTML += linha
        };

        const precoTotal = document.querySelector('.preco-total');
        precoTotal.textContent = `R$ ${total}`
    };
};

mostrarCarrinho();

async function inserirItemCarrinho(id_produto, quantidade=1) {
    const resposta = await fetch("/api/post/carrinho", {method:"POST", headers:{"Content-Type": "application/json"}, body: JSON.stringify({"id_produto":id_produto, "quantidade":quantidade})})
    if (!resposta.ok) {
        alert("Erro ao inserir item!")
    }
    mostrarCarrinho();
};