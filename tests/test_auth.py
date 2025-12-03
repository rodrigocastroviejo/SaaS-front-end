def test_login_page_loads(client):
    """Test: La página de login se carga correctamente."""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'login' in response.data.lower()

def test_login_post_simulation(client):
    """Test: Simulación de login redirige al dashboard."""
    response = client.post('/login', data={})
    assert response.status_code == 302
    assert '/dashboard' in response.location

def test_register_page_loads(client):
    """Test: La página de registro se carga correctamente."""
    response = client.get('/register')
    assert response.status_code == 200
    assert b'registro' in response.data.lower() or b'register' in response.data.lower()

def test_register_post_simulation(client):
    """Test: Simulación de registro redirige al login."""
    response = client.post('/register', data={})
    assert response.status_code == 302
    assert '/login' in response.location

def test_login_redirects_to_dashboard_with_flash(client):
    """Test: Login muestra mensaje flash y redirige."""
    response = client.post('/login', follow_redirects=True)
    assert response.status_code == 200
    # Verificar que el mensaje flash está presente
    assert b'simulado' in response.data.lower() or b'exitoso' in response.data.lower()