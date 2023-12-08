import json
from shapely.geometry import Polygon

# Coordenadas del polígono
poligono_coords = [[(-58.441296936718544, -34.56222166682468),
                    (-58.442498566357216, -34.563670645080585),
                    (-58.441296936718544, -34.56458949626034),
                    (-58.43981635734232, -34.56303451139389)]]

poligono = Polygon(poligono_coords[0])

# Cargar datos del archivo manzanas.json
with open('manzanas.json', 'r') as json_file:
    manzanas_data = json.load(json_file)

# Encontrar manzanas dentro del polígono y extraer valores 'sm'
sm_values = set()  # Usamos un conjunto para evitar duplicados
for feature in manzanas_data['features']:
    manzana_coords = feature['geometry']['coordinates'][0][0]
    manzana_polygon = Polygon(manzana_coords)
    if manzana_polygon.within(poligono):
        sm_value = feature['properties']['sm']
        sm_values.add(sm_value)

# Resultado: sm_values contiene los valores 'sm' únicos dentro del polígono
print(sm_values)
