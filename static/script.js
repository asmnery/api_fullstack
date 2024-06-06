// Função para criar usuário
document.getElementById('createUserForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  fetch('http://127.0.0.1:4000/usuarios', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          username: username,
          email: email,
          password: password
      })
  })
  .then(response => response.json())
  .then(data => {
      console.log(data);
      alert(data.mensagem);
  })
  .catch(error => console.error('Erro:', error));
});

// Função para listar usuários
document.getElementById('listUsers').addEventListener('click', function() {
  fetch('http://127.0.0.1:4000/usuarios')
  .then(response => response.json())
  .then(data => {
      console.log(data);
      const userList = document.getElementById('userList');
      userList.innerHTML = '';
      data.usuários.forEach(user => {
          const userItem = document.createElement('div');
          userItem.textContent = `ID: ${user.id}, Usuário: ${user.usuario}, Email: ${user.email}`;
          userList.appendChild(userItem);

          // Adiciona botões de atualizar e deletar
          addUserButtons(userItem, user.id);
      });
  })
  .catch(error => console.error('Erro:', error));
});

// Função para adicionar botões de atualizar e deletar a um usuário
function addUserButtons(userItem, userId) {
  const updateButton = document.createElement('button');
  updateButton.textContent = 'Atualizar';
  updateButton.addEventListener('click', function() {
      updateUser(userId);
  });
  userItem.appendChild(updateButton);

  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Deletar';
  deleteButton.addEventListener('click', function() {
      deleteUser(userId);
  });
  userItem.appendChild(deleteButton);
}

// Função para atualizar usuário
function updateUser(userId) {
  const newUsername = prompt('Digite o novo nome de usuário:');
  if (newUsername === null) return; // Usuário cancelou

  const newEmail = prompt('Digite o novo email:');
  if (newEmail === null) return; // Usuário cancelou

  fetch(`http://127.0.0.1:4000/usuarios/${userId}`, {
      method: 'PUT',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          username: newUsername,
          email: newEmail
      })
  })
  .then(response => response.json())
  .then(data => {
      console.log(data);
      alert(data.mensagem);
  })
  .catch(error => console.error('Erro:', error));
}

// Função para deletar usuário
function deleteUser(userId) {
  if (confirm('Tem certeza que deseja deletar este usuário?')) {
      fetch(`http://127.0.0.1:4000/usuarios/${userId}`, {
          method: 'DELETE'
      })
      .then(response => response.json())
      .then(data => {
          console.log(data);
          alert(data.mensagem);
      })
      .catch(error => console.error('Erro:', error));
  }
}