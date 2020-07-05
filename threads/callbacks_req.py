import logging
import threading
import requests

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)

def get_pokemon_name(response_json):
    name = response_json.get('forms')[0].get('name')
    logging.info(f'El nombre del poquemon es: {name}')

def error():
    logging.error('No fue posible realizar la acción')

def generate_request(url, success_callback, error_callback):
    response = requests.get(url)

    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()

if __name__ == "__main__":
    thread_1 = threading.Thread(target=generate_request, kwargs={'url':'https://pokeapi.co/api/v2/pokemon/1/',
                                                                'success_callback': get_pokemon_name,
                                                                'error_callback': error
                                                            })
    thread_1.start()