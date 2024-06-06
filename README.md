
# Impacstock - Gerenciamento de Produtos (ANDAMENTO)

Um projeto que busca gerenciar produtos de diversos setores, se baseando no controle de estoque com funções básicas como criar novos produtos, listar todos os produtos ou um produto separamente, atualizar produtos pelo nome, valor ou quantidade no estoque e também a exclusão de produtos já cadastrados.




## Documentação da API


#### Cria um produto

```http
    POST localhost:4000/produtos
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome` | `string` | Nome do produto |
| `preço` | `int` | Preço do produto |
| `quantidade` | `int` | Quantidade do produto |

#### Lista todos os produtos

```http
  GET localhost:4000/produtos
```


#### Lista um produto

```http
  GET localhost:4000/produtos/{id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | ID do item que você quer listar |


#### Atualiza um produto

```http
  PUT localhost:4000/produtos/{id} - ID do item que você quer atualizar
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome` | `string` | Nome do produto |
| `preço` | `int` | Preço do produto |
| `quantidade` | `int` | Quantidade do produto |


#### Deleta um produto

```http
  GET localhost:4000/produtos/{id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | ID do item que você quer listar |


## Autores

- [@asmnery](https://www.github.com/asmnery)
- [@GustavoHoiti](https://github.com/GustavoHoiti)

