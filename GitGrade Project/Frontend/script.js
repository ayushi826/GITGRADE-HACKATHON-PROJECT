async function analyze() {
    const url = document.getElementById("repoUrl").value;

    if (!url) {
        alert("Please enter a GitHub repo URL!");
        return;
    }

    const outputCard = document.getElementById("output");
    const resultText = document.getElementById("resultText");
    
    resultText.textContent = "Analyzing... Please wait ⏳";

    outputCard.classList.remove("hidden");

    try {
        const res = await fetch(`http://127.0.0.1:8000/analyze?url=${url}`);

        const data = await res.json();

        resultText.textContent = JSON.stringify(data, null, 2);

    } catch (error) {
        resultText.textContent = "❌ Error: Unable to connect to backend";
    }
}
