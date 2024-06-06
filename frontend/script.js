document.getElementById('add-product-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const nome = document.getElementById('product-name').value;
    const preço = parseFloat(document.getElementById('product-price').value);
    const quantidade = parseInt(document.getElementById('product-quantity').value);

    fetch('http://127.0.0.1:4000/produtos')
        .then(response => response.json())
        .then(data => {
            const produtos = data.produtos;
            const produtoExistente = produtos.find(produto => produto.nome === nome);

            if (produtoExistente) {
                alert('Um produto com o mesmo nome já existe!');
            } else {
                fetch('http://127.0.0.1:4000/produtos', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        nome: nome,
                        preço: preço,
                        quantidade: quantidade
                    })
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    alert(data.mensagem);
                    fetchProducts(); 
                })
                .catch(error => console.error('Erro:', error));
            }
        })
        .catch(error => console.error('Erro:', error));
});


function fetchProducts() {
    fetch('http://127.0.0.1:4000/produtos')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        const productList = document.getElementById('product-list');
        productList.innerHTML = '';
        data.produtos.forEach(product => {
            const productRow = document.createElement('tr');
            productRow.innerHTML = `
                <td>${product.id}</td>
                <td>${product.nome}</td>
                <td>${product.preço}</td>
                <td>${product.quantidade}</td>
                <td class="product-buttons">
                    <button class="update" onclick="updateProduct(${product.id})">Atualizar</button>
                    <button class="delete" onclick="deleteProduct(${product.id})">Deletar</button>
                </td>
            `;
            productList.appendChild(productRow);
        });

        document.querySelectorAll('.update').forEach(button => {
            button.style.backgroundColor = '#4CAF50';
            button.style.color = 'white';
        });

        document.querySelectorAll('.delete').forEach(button => {
            button.style.backgroundColor = '#f44336';
            button.style.color = 'white';
        });
    })
    .catch(error => console.error('Erro:', error));
}
function updateProduct(productId) {
    const newNome = prompt('Digite o novo nome do produto:');
    if (newNome === null) return; 

    const newPreço = parseFloat(prompt('Digite o novo preço do produto:'));
    if (isNaN(newPreço)) return;

    const newQuantidade = parseInt(prompt('Digite a nova quantidade do produto:'));
    if (isNaN(newQuantidade)) return;

    fetch(`http://127.0.0.1:4000/produtos/${productId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome: newNome,
            preço: newPreço,
            quantidade: newQuantidade
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert(data.mensagem);
        fetchProducts();
    })
    .catch(error => console.error('Erro:', error));
}
function deleteProduct(productId) {
    if (confirm('Tem certeza que deseja deletar este produto?')) {
        fetch(`http://127.0.0.1:4000/produtos/${productId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert(data.mensagem);
            fetchProducts();
        })
        .catch(error => console.error('Erro:', error));
    }
}

fetchProducts();
