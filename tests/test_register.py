import requests
import pytest

# Register successful
register_url = "https://reqres.in/api/register"
payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}


def test_register_successful():
    response = requests.post(register_url, data=payload)

    print(response.status_code)
    print(response.json())