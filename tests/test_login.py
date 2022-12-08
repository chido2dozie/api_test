import pytest
import requests


# Login successfully
login_url = "https://reqres.in/api/login"
login_payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}


def test_login_successful():
    response = requests.post(login_url, data=login_payload)
    print(response.status_code)
    print(response.json())