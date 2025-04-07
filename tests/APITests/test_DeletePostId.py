import requests

def test_deletePost():
    id = 1
    url = f"https://jsonplaceholder.typicode.com/posts/1{id}"


    response = requests.delete(url)

    # verify the correct response status code is returned and ID deleted
    assert response.status_code == 200
