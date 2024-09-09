// script.js
document.addEventListener('DOMContentLoaded', () => {
    const runButton = document.getElementById('run-button');
    const codeEditor = document.getElementById('code-editor');
    const outputDiv = document.getElementById('output');

    runButton.addEventListener('click', async () => {
        const code = codeEditor.value;

        try {
            const response = await fetch('http://localhost:5000/run', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ code })
            });

            const result = await response.json();
            outputDiv.textContent = result.output;
        } catch (error) {
            outputDiv.textContent = 'Error executing code: ' + error.message;
        }
    });
});
