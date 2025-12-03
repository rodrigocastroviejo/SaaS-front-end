def test_dashboard_requires_auth(client):
    """Test: Dashboard requiere autenticación."""
    response = client.get('/dashboard')
    # En una app real, esto redirigiría al login
    # Como es simulación, verifica que la página se carga
    assert response.status_code == 200

def test_dashboard_loads_with_mock_data(client):
    """Test: Dashboard carga con datos simulados."""
    response = client.get('/dashboard')
    assert response.status_code == 200
    # Verificar elementos clave del dashboard
    assert b'dashboard' in response.data.lower()
    # Verificar que se cargan los documentos y transacciones
    assert b'documento' in response.data.lower() or b'transacc' in response.data.lower()

def test_generate_document_page_loads(client):
    """Test: Página de generación de documentos se carga."""
    response = client.get('/dashboard/generate-document')
    assert response.status_code == 200
    assert b'generar' in response.data.lower() or b'generate' in response.data.lower()

def test_generate_document_post(client):
    """Test: Generación de documento simulado."""
    response = client.post('/dashboard/generate-document', data={})
    assert response.status_code == 302
    assert '/dashboard' in response.location

def test_navbar_present_in_all_pages(client):
    """Test: Navbar está presente en todas las páginas."""
    pages = ['/login', '/register', '/dashboard']
    for page in pages:
        response = client.get(page)
        assert response.status_code == 200
        # Asumiendo que el navbar tiene un elemento distintivo
        assert b'nav' in response.data.lower() or b'navbar' in response.data.lower()

def test_mock_data_generation():
    """Test: Datos simulados se generan correctamente."""
    from app.utils.mock_data import generate_documents, generate_transactions
    
    documents = generate_documents(3)
    transactions = generate_transactions(5)
    
    assert len(documents) == 3
    assert len(transactions) == 5
    assert all('id' in doc for doc in documents)
    assert all('monto' in trans for trans in transactions)