def test_static_files_served(client):
    """Test: Archivos estáticos se sirven correctamente."""
    # Test para CSS
    response = client.get('/static/css/main.css')
    assert response.status_code == 200
    assert 'text/css' in response.content_type
    
    # Test para JS
    response = client.get('/static/js/theme-toggle.js')
    assert response.status_code == 200
    assert 'application/javascript' in response.content_type

def test_templates_components():
    """Test: Componentes de templates existen."""
    import os
    # Verificar que los templates base existen
    assert os.path.exists('app/templates/base.html')
    assert os.path.exists('app/templates/components/navbar.html')
    assert os.path.exists('app/templates/components/footer.html')