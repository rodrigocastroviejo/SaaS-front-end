def test_dashboard_page(client):
    # Primero "loguearnos" (redirige a dashboard)
    client.post('/auth/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    })
    
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data
    assert b'Saldo Actual' in response.data
    assert b'Documentos Generados' in response.data

def test_generate_document_page(client):
    client.post('/auth/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    })
    
    response = client.get('/generate-document')
    assert response.status_code == 200
    assert b'Generar Nuevo Documento' in response.data
    assert b'Tipo de Documento' in response.data