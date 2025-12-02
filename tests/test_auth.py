def test_login_page(client):
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert b'Iniciar Sesión' in response.data
    assert b'Email' in response.data
    assert b'Contraseña' in response.data

def test_register_page(client):
    response = client.get('/auth/register')
    assert response.status_code == 200
    assert b'Registro' in response.data
    assert b'Nombre' in response.data

def test_login_post_redirect(client):
    response = client.post('/auth/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=False)
    assert response.status_code == 302
    assert '/dashboard' in response.location