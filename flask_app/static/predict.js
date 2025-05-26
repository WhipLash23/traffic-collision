document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = [];
    formData.forEach((value) => {
        data.push(Number(value));
    });

    fetch('/make_prediction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        const predictionResult = document.getElementById('predictionResult');
        predictionResult.textContent = `Prediction: ${result.prediction}`;
        predictionResult.classList.remove('hidden');
    });
});
