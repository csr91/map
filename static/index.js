const toggleBtn = document.getElementById('toggleBtn');
const navLinks = document.querySelector('.nav-links');


document.addEventListener('DOMContentLoaded', function () {
    var map = L.map('map-container').setView([-34.5632, -58.4117], 15);
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
    
    var drawnItems = new L.FeatureGroup();
    map.addLayer(drawnItems);
    
    var drawControl = new L.Control.Draw({
        draw: {
            polygon: true,
            polyline: false,
            circle: false,
            marker: false,
            rectangle: false
        },
        edit: {
            featureGroup: drawnItems,
            remove: true
        }
    });
    map.addControl(drawControl);
    
    var coordinates; // Variable para almacenar las coordenadas
    
    map.on('draw:created', function (e) {
        var layer = e.layer;
        drawnItems.addLayer(layer);
        
        coordinates = layer.getLatLngs();
        document.getElementById('coordinates').innerText = 'Coordenadas del polígono: ' + JSON.stringify(coordinates);
    });
    
    var enviarBtn = document.getElementById('enviarBtn');
    enviarBtn.addEventListener('click', function() {
        if (coordinates) {
            // Enviar las coordenadas al servidor Flask cuando se hace clic en el botón
            fetch('/calcular_sm', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(coordinates)
            })
            .then(response => response.json())
            .then(data => {
                // Manejar la respuesta del servidor
                console.log('Las manzanas son:', data);   
                     // Actualizar el contenido del elemento con la respuesta del servidor
                var respuestaServidorElement = document.getElementById('respuesta-servidor');
                respuestaServidorElement.innerText = 'Respuesta del servidor: ' + JSON.stringify(data);
            })
            .catch(error => {
                // Manejar errores de la solicitud
                console.error('Error:', error);
            });
        } else {
            // No hay polígono dibujado, maneja este caso según sea necesario
            console.log('Dibuja un polígono antes de enviar las coordenadas.');
        }
    });
});

