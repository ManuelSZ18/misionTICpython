import requests

if __name__ == '__main__':
    url = 'https://www.datos.gov.co/resource/rejx-ewy7.json'
    args = {'municipio' : 'SUAZA'}
    response = requests.get(url, params = args)

    if response.status_code == 200:
        payload = response.json()
        results = payload
        
        if results:
            for result in range(0, len(results)):
                latitude = results[result].get('coordenadas_de_referencia')
                longitude = results[result].get('coordenadas_de_referencia_1')
                activeUsers = results[result].get('n_usuarios_activos_mes')
                print('En las coordenadas de latitud {} y longitud {} hay {} usuarios activos al mes.'.format(latitude, longitude, activeUsers))
            