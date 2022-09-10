import ast
import pytest
import requests
from pytest_bdd import given, when, then, parsers, scenarios
import json

scenarios("../features/api_crud_user.feature")


@given(parsers.re("I log in as '(?P<admin>.*)' with '(?P<password>.*)'"
                  " on the '(?P<api_url>.*)' resource"))
def set_rest_api_url(request, admin, password, api_url):
    pytest.globalDict = {'api_url': api_url, 'login': admin,
                         'password': password}


@given(parsers.re("I set '(?P<users>.*)' api endpoint"))
def setup_users_endpoint(request, users):
    pytest.globalDict['users_endpoint'] = \
        f"{pytest.globalDict['api_url']}{users}"


@when(parsers.re("I send POST HTTP request with '(?P<payload>.*)'"))
def send_post_request(request, payload):
    url = pytest.globalDict['users_endpoint']
    data = json.loads(eval(payload))
    response_post = requests.post(url, data,
                                  auth=(pytest.globalDict['login'],
                                        pytest.globalDict['password']))
    request.session.globalDict = {'user_uniq_id': response_post.json()['url']}
    pytest.response = response_post


@then(parsers.re("I receive valid HTTP response code '(?P<status_code>.*)'"))
def get_status_code(request, status_code):
    response = pytest.response
    assert response.status_code == int(status_code), print(response.json())


@when("I send GET HTTP request to unique user endpoint")
def send_get_request(request):
    url = request.session.globalDict['user_uniq_id']
    response_get = requests.get(url,
                                auth=(pytest.globalDict['login'],
                                      pytest.globalDict['password']))
    pytest.response = response_get


@then(parsers.re("I receive valid HTTP response with '(?P<payload>.*)'"))
def valid_payload_response(request, payload):
    response = pytest.response
    data = json.loads(eval(payload))
    assert data['username'] in str(response.json())


@when(parsers.re("I send PUT HTTP request with '(?P<payload>.*)'"
                 " to unique user endpoint"))
def send_put_request(request, payload):
    url = request.session.globalDict['user_uniq_id']
    update_data_user = json.loads(eval(payload))
    response_put = requests.put(url, update_data_user,
                                auth=(pytest.globalDict['login'],
                                      pytest.globalDict['password']))
    pytest.response = response_put


@when("I send DELETE HTTP request to unique user endpoint")
def send_delete_request(request):
    url = request.session.globalDict['user_uniq_id']
    response_delete = requests.delete(url, auth=(pytest.globalDict['login'],
                                                 pytest.globalDict[
                                                     'password']))
    pytest.response = response_delete