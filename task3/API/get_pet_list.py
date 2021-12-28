import requests

get_headers_my_pets = {
    'auth_key ': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'filter': 'my_pets'
}

get_params_my_pets = get_headers_my_pets

my_pets_link = 'https://petfriends1.herokuapp.com/api/pets?filter=my_pets'


def get_pets_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(get_pets_list(my_pets_link, get_params_my_pets, get_headers_my_pets))

