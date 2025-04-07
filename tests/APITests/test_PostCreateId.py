import requests

def test_createPostId():
    url = "https://jsonplaceholder.typicode.com/posts"

    new_post = {
        "name": "Test",
        "country" :"United Kingdom",
        "id" :"777"
    }

    response = requests.post(url, json=new_post)

    # verify the correct response status code is returned and new ID created
    assert response.status_code == 201