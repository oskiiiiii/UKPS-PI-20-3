import requests

post_new_pet_headers = {
    'auth_key': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'name': 'Marsel',
    'animal_type': 'cat',
    'age': '6',
    'pet_photo': ''}

post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"


def post_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={'pet_photo': open('cat.jpg', 'rb')}
                             )
    if response.status_code == 200:
        print('OK')

    if response.ok:
        print('OK')

    return response.text


print(post_new_pet(new_pet_POST_link, post_new_pet_params, post_new_pet_headers))

