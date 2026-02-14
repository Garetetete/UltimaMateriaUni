import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from fastapi.testclient import TestClient
from app.main import app

scenarios('features/valid.feature')

@pytest.fixture
def client():
    return TestClient(app)
@pytest.fixture
def context():
    return {}
@given(parsers.parse('I have a number "{number}"'))
def given_number(context, number):
    context['number'] = number
@when('I validate the number')
def when_validate_number(client, context):
    response = client.get(f"/validate/{context['number']}")
    context['response'] = response

@then(parsers.parse('the result should be "{result}"'))
def then_result(context, result):
    assert context['response'].status_code == 200
    assert context['response']['valid'] == result