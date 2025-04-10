function sendMessage() {
    const input = document.getElementById('user-input');
    const chatHistory = document.getElementById('chat-history');
    
    // Exibir mensagem do usuário
    chatHistory.innerHTML += `<div class="user-message">Você: ${input.value}</div>`;
    
    fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input.value })
    })
    .then(response => response.json())
    .then(data => {
        chatHistory.innerHTML += `<div class="bot-message">Bot: ${data.response}</div>`;
        input.value = '';
        chatHistory.scrollTop = chatHistory.scrollHeight;
    });
}

// Permitir Enter para enviar
document.getElementById('user-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});