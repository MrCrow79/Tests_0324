import pytest
from lessons.lesson_15.phone import Phone


@pytest.fixture
def get_new_phone(default_model, default_brand):
    return Phone(default_brand, default_model)


@pytest.fixture(scope='session', autouse=False)
def get_model():
    print('get_model fixture')
    return 'Iphone 13'


@pytest.fixture(scope='session', autouse=False)
def get_brand():
    print('get_brand fixture')
    return 'Apple'


@pytest.fixture(scope='session')
def get_new_phone_session(get_brand, get_model):
    return Phone(get_brand, get_model)


@pytest.fixture(scope='module', autouse=False)  # by default (scope='function', autouse=False)
def get_new_phone2(get_brand, get_model):
    print('get_new_phone2 fixture')
    return Phone(get_brand, get_model)


@pytest.fixture(scope='function', autouse=True)
def clear_call_history(get_new_phone2):
    yield
    print('clear_call_history fixture')
    get_new_phone2.clear_call_history()
