<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mapa con Polígonos</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
  <style>
    #map {
      height: 500px;
    }
  </style>
</head>

<body>
  <div id="map"></div>

  <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
  <script>
    var map = L.map('map').setView([-34.565, -58.44], 15);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    var polygons = [
      // Inserta aquí los polígonos proporcionados en tu pregunta
    ];

    polygons.forEach(function (polygonCoords) {
      var polygon = L.polygon(polygonCoords.coordinates, {
        color: 'blue',
        fillOpacity: 0.5
      }).addTo(map);
    });
  </script>
</body>

</html>
