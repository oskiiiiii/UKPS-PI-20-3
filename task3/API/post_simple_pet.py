import requests

post_simple_headers = {
    'auth_key': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'name': 'Alex',
    'animal_type': 'dog',
    'age': '3'
}

post_simple_params = post_simple_headers
create_pet_simple_POST_link = 'https://petfriends1.herokuapp.com/api/create_pet_simple'


def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )

    if response.status_code == 200:
        print('OK')

    if response.ok:
        print('OK')

    print(type(response), type(response.ok))
    return response.ok


print(post_simple_pet(create_pet_simple_POST_link, post_simple_params, post_simple_headers))
