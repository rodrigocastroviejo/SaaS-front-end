import pytest
from app import create_app

@pytest.fixture
def app():
    """Fixture para crear la aplicación de prueba."""
    app = create_app()
    app.config.update({
        'TESTING': True,
        'WTF_CSRF_ENABLED': False,  # Deshabilitar CSRF para testing
    })
    return app

@pytest.fixture
def client(app):
    """Fixture para el cliente de pruebas."""
    return app.test_client()

@pytest.fixture
def auth_client(client):
    """Cliente autenticado (simulado)."""
    # Simular una sesión de usuario
    with client.session_transaction() as session:
        session['user_id'] = 1
        session['_fresh'] = True
    return client