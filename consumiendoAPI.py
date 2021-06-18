from numpy import copy
import requests
import numpy as np

if __name__ == '__main__':
    url = 'https://www.datos.gov.co/resource/rejx-ewy7.json'
    args = {'municipio' : 'SUAZA'}
    response = requests.get(url, params = args)

    if response.status_code == 200:
        payload = response.json()
        results = payload
        
        if results:
            result = 0            
            latitude = str(results[result].get('coordenadas_de_referencia'))
            longitude = str(results[result].get('coordenadas_de_referencia_1'))
            activeUsers = str(results[result].get('n_usuarios_activos_mes')) 
            zonesWifi = np.array([[latitude, longitude, activeUsers]])
            while len(zonesWifi) < len(results):
                latitude = str(results[result].get('coordenadas_de_referencia'))
                longitude = str(results[result].get('coordenadas_de_referencia_1'))
                activeUsers = str(results[result].get('n_usuarios_activos_mes'))   
                zonesWifi = np.append(zonesWifi, [[latitude, longitude, activeUsers]], axis = 0)
                result = result + 1
print(zonesWifi)