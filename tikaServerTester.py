import requests

tika_server_url = 'http://localhost:9998'

try:
    response = requests.get(tika_server_url)
    if response.status_code == 200:
        print('O servidor Tika está respondendo corretamente.')
    else:
        print('Falha na comunicação com o servidor Tika. Status code:', response.status_code)
except requests.exceptions.RequestException as e:
    print('Erro ao tentar se comunicar com o servidor Tika:', e)
