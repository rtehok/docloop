import pytest

from src.app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['MAX_CONTENT_LENGTH'] = 1024
    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client
