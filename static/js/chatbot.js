const form = document.getElementById('chat-form');
const chatBox = document.getElementById('chat-box');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const userInput = document.getElementById('user-input').value;

    // Display user message
    chatBox.innerHTML += `<div class='text-right mb-2'><span class='inline-block bg-blue-500 text-white px-4 py-2 rounded-lg'>${userInput}</span></div>`;

    try {
        // Send message to the server
        const response = await fetch('/chatbot', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userInput })
        });

        const data = await response.json();
        if (data.reply) {
            chatBox.innerHTML += `<div class='text-left mb-2'><span class='inline-block bg-gray-200 px-4 py-2 rounded-lg'>${data.reply}</span></div>`;
        } else {
            chatBox.innerHTML += `<div class='text-left mb-2 text-red-500'>Error: ${data.error}</div>`;
        }
    } catch (error) {
        chatBox.innerHTML += `<div class='text-left mb-2 text-red-500'>Error: Unable to connect to the server. Please try again later.</div>`;
    }

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;

    // Clear input
    document.getElementById('user-input').value = '';
});
