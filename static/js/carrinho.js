async function mostrarCarrinho() {
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")

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
                        <img src="${dado.imagem}" alt="${dado.nome}" class="item-imagem">
                    </div>
                    <div class="item-info">
                        <span class="item-nome">${dado.nome}</span>
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