import requests

def test_getPostId():
    id = 20 # take any id as they range from 1 - 100
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"

    response = requests.get(url)

    # verify the correct response status code is returned to the end user + request
    assert response.status_code == 200


def test_getPostIdBadData():
    id = 888777 # id doesn't exist # bad data
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"

    response = requests.get(url)

    # verify the correct response status code is returned to the end user + request
    assert response.status_code == 404