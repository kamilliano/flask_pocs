from app import create_app
import pytest

#This is a fixture that is required to mock Flask app
#so you can access client, app object
@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app
