mapboxgl.accessToken = mapboxToken;

const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/standard',
    center: [-56.0967, -15.6014], // Cuiabá
    zoom: 16,
    pitch: 60
});

let markers = [];
let coordsArray = [];
let isLocked = false; 

map.on('click', (e) => {
    if (isLocked) return; 

    const { lng, lat } = e.lngLat;
    const marker = new mapboxgl.Marker({ color: "#e74c3c" }).setLngLat([lng, lat]).addTo(map);
    
    markers.push(marker);
    coordsArray.push(`${lng},${lat}`);

    if (coordsArray.length >= 2) {
        showConfirmation();
    }
});

function showConfirmation() {
    isLocked = true;
    document.getElementById('controls').style.display = 'block';
    document.getElementById('results').innerHTML = `<strong>${coordsArray.length} pontos selecionados.</strong>`;
}

function continueEditing() {
    isLocked = false;
    document.getElementById('controls').style.display = 'none';
    document.getElementById('results').innerText = "Continue a clicar no mapa...";
}

async function confirmSave() {
    const coordsString = coordsArray.join(';');
    
    document.getElementById('results').innerText = "A guardar no histórico...";

    try {
        const response = await fetch('/calculate_matrix', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ coords: coordsString })
        });
        
        if (response.ok) {
            alert("Sucesso! Dados salvos no historico_rotas.json");
            clearPoints(); 
        }
    } catch (error) {
        alert("Erro ao salvar dados.");
    }
}

function clearPoints() {
    markers.forEach(m => m.remove());
    markers = [];
    coordsArray = [];
    isLocked = false;
    document.getElementById('controls').style.display = 'none';
    document.getElementById('results').innerText = "Aguardando marcações...";
}