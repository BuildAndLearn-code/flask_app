// Path: flask_app/static/script.js
async function runCode() {
    const code = document.getElementById("code").value;
    const outputElement = document.getElementById("output");

    try {
        const response = await fetch("/execute", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ code })
        });

        const result = await response.json();
        outputElement.textContent = result.output || result.error;
    } catch (error) {
        outputElement.textContent = "An error occurred: " + error.message;
    }
}
