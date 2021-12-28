import requests

post_set_photo_headers = {
    'auth_key': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'pet_id': '3376911c-eab6-48c2-a759-6ad97ae85fa7'}

post_set_photo_params = post_set_photo_headers
set_photo_POST_link = 'https://petfriends1.herokuapp.com/api/pets/set_photo/' + '588734bd-742c-4b32-b021-b89259037ea7'


def post_set_photo(link, post_params, post_headers):
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


print(post_set_photo(set_photo_POST_link, post_set_photo_params, post_set_photo_headers))

