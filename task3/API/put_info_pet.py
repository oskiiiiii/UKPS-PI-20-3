import requests

put_info_headers = {
    'auth_key': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'pet_id': '588734bd-742c-4b32-b021-b89259037ea7'
}

put_info_params = put_info_headers
put_info_link = 'https://petfriends1.herokuapp.com/api/pets/' + '588734bd-742c-4b32-b021-b89259037ea7'


def put_pet_info(link, p_params, p_headers):
    response = requests.put(link,
                            params=p_params,
                            headers=p_headers
                            )
    if response.status_code == 200:
        print('OK')

    if response.ok:
        print('OK')

    return response.text


print(put_pet_info(put_info_link, put_info_params, put_info_headers))