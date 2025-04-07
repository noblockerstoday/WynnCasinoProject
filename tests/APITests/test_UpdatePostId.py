import requests

def test_UpdatePostPut():
    id = 1
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"


    new_data = {
        "name": "Test",
        "country" :"United",
        "id" :"1"
    }

    response = requests.put(url, json=new_data)

    # verify the correct response status code is returned and data is fully updated
    assert response.status_code == 200



import requests

def test_UpdatePostPacth():
    id = 2
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"


    new_data = {
        "name": "Tested",
        "country" :"United",
        "id" :"2"
    }

    response = requests.patch(url, json=new_data)

    # verify the correct response status code is returned and data is partially updated
    assert response.status_code == 200

