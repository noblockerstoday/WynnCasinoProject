import requests

def test_getPost():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    # verify the correct response status code is returned to the end user + request
    assert response.status_code == 200