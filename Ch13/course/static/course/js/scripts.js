const button = document.getElementById('greet-btn');
const message = document.getElementById('message');

button.addEventListener('click', function () {
    message.textContent = 'Hello from JavaScript! This script was loaded as a static file.';
});
