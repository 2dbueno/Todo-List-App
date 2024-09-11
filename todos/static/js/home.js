// Obtém o modal e os botões
const modal = document.getElementById('confirmationModal');
const confirmBtn = document.getElementById('confirmBtn');
const cancelBtn = document.getElementById('cancelBtn');
const logoutButton = document.querySelector('.logout-button');

// Abre o modal
logoutButton.addEventListener('click', function (event) {
    event.preventDefault(); // Impede o envio do formulário
    modal.style.display = 'block'; // Mostra o modal
});

// Fecha o modal e cancela a ação
cancelBtn.addEventListener('click', function () {
    modal.style.display = 'none'; // Oculta o modal
});

// Confirma a ação e envia o formulário
confirmBtn.addEventListener('click', function () {
    document.querySelector('.logout-button').closest('form').submit(); // Envia o formulário
});

// Fecha o modal se o usuário clicar fora dele
window.addEventListener('click', function (event) {
    if (event.target === modal) {
        modal.style.display = 'none'; // Oculta o modal
    }
});
