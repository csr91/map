from flask import request, jsonify
import json
from shapely.geometry import Polygon
import requests  # Importar la biblioteca 'requests' para hacer solicitudes HTTP
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Agregar CORS a la aplicación Flask

# URL del archivo GeoJSON
geojson_url = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/secretaria-de-desarrollo-urbano/manzanas/mapa_manzanas.geojson"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_sm', methods=['POST'])
def calcular_sm():
    data = request.get_json()  # Obtener datos JSON del cuerpo de la solicitud
    coordinates = data[0]  # Obtener las coordenadas del polígono del cuerpo de la solicitud

    # Formatear las coordenadas al formato necesario para crear el objeto Polygon
    formatted_coordinates = [tuple([coord['lng'], coord['lat']]) for coord in coordinates]

    poligono = Polygon(formatted_coordinates)

    # Hacer solicitud HTTP para obtener el contenido del archivo GeoJSON desde la URL
    response = requests.get(geojson_url)
    manzanas_data = response.json()

    # Encontrar manzanas dentro del polígono y extraer valores 'sm'
    sm_values = set()  # Usamos un conjunto para evitar duplicados
    for feature in manzanas_data['features']:
        manzana_coords = feature['geometry']['coordinates'][0][0]
        manzana_polygon = Polygon(manzana_coords)
        if manzana_polygon.within(poligono):
            sm_value = feature['properties']['sm']
            sm_values.add(sm_value)

    # Resultado: sm_values contiene los valores 'sm' únicos dentro del polígono
    return jsonify(list(sm_values)), 200

if __name__ == '__main__':
    app.run(debug=True)
