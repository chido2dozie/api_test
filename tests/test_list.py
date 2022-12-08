import requests
import pytest

# List resource
list_url = "https://reqres.in/api/unknown"


def test_list_resource():
    response = requests.get(list_url)
    print(response.status_code)
    print(response.json())

    # assert response
    response_json = response.json()
    assert response_json['data'][2]['id'] == 3

