document.addEventListener('DOMContentLoaded', function() {
    const cidadeInput = document.getElementById('cidade');
    const verificarBtn = document.getElementById('verificar-btn');
    const previsaoTempoDiv = document.getElementById('previsao-tempo1');

    verificarBtn.addEventListener('click', function() {
        const cidade = cidadeInput.value.trim();

        if (cidade !== '') {
            obterPrevisaoTempo(cidade);
        } else {
            previsaoTempoDiv.innerHTML = '<p>Por favor, insira o nome da cidade.</p>';
        }
    });

    function obterPrevisaoTempo(cidade) {
        // Implemente a lógica para fazer solicitações à API de previsão do tempo
        // e receber os dados de previsão usando a chave de API fornecida
        const apiKey = '8197995a86d1d31479e30ec445ed6635';
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${cidade}&appid=${apiKey}&units=metric`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                const temperatura = data.main.temp;
                const condicao = data.weather[0].description;
                const cidadeNome = data.name;

                const previsaoTempoHTML = `
                    <h2>Previsão do Tempo em ${cidadeNome}</h2>
                    <p>Temperatura: ${temperatura}°C</p>
                    <p>Condição: ${condicao}</p>
                `;

                previsaoTempoDiv.innerHTML = previsaoTempoHTML;
            })
            .catch(error => {
                previsaoTempoDiv.innerHTML = '<p>Ocorreu um erro ao obter a previsão do tempo.</p>';
                console.error('Erro:', error);
            });
    }
});
