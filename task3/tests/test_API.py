import pytest
import requests

# ПАРАМЕТРЫ

# POST PET SIMPLE
post_simple_headers = {
    'auth_key': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'name': 'Apex',
    'animal_type': 'floor',
    'age': '2018'
}
post_simple_params = post_simple_headers
create_pet_simple_POST_link = 'https://petfriends1.herokuapp.com/api/create_pet_simple'

# API KEY
get_key_headers = {
    'email': 'oski@mail.ru',
    'password': '123123'
}
get_key_params = get_key_headers
api_key_link = 'https://petfriends1.herokuapp.com/api/key'

# PETS LIST
get_headers_my_pets = {
    'auth_key ': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'filter': 'my_pets'
}
get_params_my_pets = get_headers_my_pets
my_pets_link = 'https://petfriends1.herokuapp.com/api/pets?filter=my_pets'

# NEW PET
post_new_pet_headers = {
    'auth_key': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'name': 'Fluffy',
    'animal_type': 'cat',
    'age': '14',
    'pet_photo': ''
}
post_new_pet_params = post_new_pet_headers
new_pet_POST_link = 'https://petfriends1.herokuapp.com/api/pets'

# SET PHOTO
post_set_photo_headers = {
    'auth_key': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'pet_id': '098833f-649e-48d6-b90e-46206548fa18'
}
post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + "588734bd-742c-4b32-b021-b89259037ea7"

# DELETE
delete_pet_headers = {
    'auth_key': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'pet_id': '3376911c-eab6-48c2-a759-6ad97ae85fa7'
}
delete_pet_params = delete_pet_headers
DELETE_pet_link = 'https://petfriends1.herokuapp.com/api/pets/' + "b965e1b9-0611-4692-aaf0-15bec3504cf2"

# PUT INFO
put_info_headers = {
    'auth_key': '52081f91e869bc9b6d8dfa0b317fb91f1ff7f669553e1a447289f1c6',
    'pet_id': '7cf41de9-0c61-4053-ac88-9968a518a303'
}
put_info_params = put_info_headers
put_info_link = 'https://petfriends1.herokuapp.com/api/pets/' + '7cf41de9-0c61-4053-ac88-9968a518a303'


# ФИКСТУРЫ
@pytest.fixture
def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )
    return response.ok


@pytest.fixture
def get_api_key(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def get_pets_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def post_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('cat.jpg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def post_set_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('dog.jpg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        return True


@pytest.fixture
def put_pet_info():
    response = requests.put(put_info_link,
                            params=put_info_params,
                            headers=put_info_headers
                            )
    return response.ok


# ТЕСТЫ
@pytest.mark.parametrize('link, params, header, expected_result',
                         [  # post_simple_pet
                             (create_pet_simple_POST_link, post_simple_params, post_simple_headers, True),

                             # post_new_pet
                             (new_pet_POST_link, post_new_pet_params, post_new_pet_headers, False),

                             # post_set_photo
                             pytest.param(set_photo_POST_link, post_set_photo_params, post_set_photo_headers, True,
                                          marks=pytest.mark.xfail),

                         ]
                         )
def test_post(link, params, header, expected_result):
    response = requests.post(link,
                             params=params,
                             headers=header
                             )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [  # get_api_key
                             (api_key_link, get_key_params, get_key_headers, True),

                             # get_my_pets_list
                             (my_pets_link, get_params_my_pets, get_headers_my_pets, True)
                         ]
                         )
def test_get(link, params, header, expected_result):
    response = requests.get(link,
                            params=params,
                            headers=header
                            )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (DELETE_pet_link, delete_pet_params, delete_pet_headers, True)
                         ]
                         )
def test_delete(link, params, header, expected_result):
    response = requests.delete(link,
                               params=params,
                               headers=header
                               )
    assert response.ok == expected_result


def test_put(put_pet_info):
    assert put_pet_info == True