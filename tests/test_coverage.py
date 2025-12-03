def test_blueprints_registered(app):
    """Test: Blueprints están registrados correctamente."""
    # Verificar que los blueprints están en la aplicación
    assert 'auth' in app.blueprints
    assert 'dashboard' in app.blueprints
    
    # Verificar rutas específicas
    url_map = list(app.url_map.iter_rules())
    urls = {str(rule) for rule in url_map}
    
    assert '/login' in urls
    assert '/register' in urls
    assert '/dashboard' in urls
    assert '/dashboard/generate-document' in urls

# def test_secret_key_set(app):
#     """Test: Secret key está configurada."""
#     assert app.config['SECRET_KEY'] is not None
#     assert app.config['SECRET_KEY'] != 'dev-key-change-in-production'  # En producción

def test_response_headers(client):
    """Test: Headers de respuesta son correctos."""
    response = client.get('/login')
    assert 'Content-Type' in response.headers
    assert 'text/html' in response.headers['Content-Type']