# 📊 SaaS Frontend - Panel de Gestión de Documentos

Un frontend SaaS moderno y responsivo para la gestión de documentos y transacciones, construido con Flask y Flowbite.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey.svg)
![Docker](https://img.shields.io/badge/Docker-Compatible-2496ED.svg)
![Railway](https://img.shields.io/badge/Railway-Deployed-0B0D0E.svg)

## 🚀 Demostración en Vivo

**Accede a la aplicación desplegada:**  
[https://saas-front-end-production.up.railway.app/login](https://saas-front-end-production.up.railway.app/login)

## ✨ Características

- 🔐 **Autenticación** - Pantallas de login y registro (interfaz visual)
- 📊 **Dashboard** - Panel principal con métricas ficticias
- 📄 **Gestión de Documentos** - Listado y generación de documentos
- 💳 **Gestión de Saldo** - Visualización de transacciones y recargas
- 🌓 **Tema Oscuro/Claro** - Con persistencia de preferencias
- 📱 **Diseño Responsivo** - Optimizado para móvil y escritorio
- 🐳 **Contenedorizado** - Listo para Docker y despliegue en Railway

## 🏗️ Estructura del Proyecto

```
.
├── Dockerfile
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── __init__.cpython-311.pyc
│   ├── blueprints
│   │   ├── auth
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   └── routes.cpython-311.pyc
│   │   │   ├── routes.py
│   │   │   └── templates
│   │   │       └── auth
│   │   │           ├── login.html
│   │   │           └── register.html
│   │   └── dashboard
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       │   ├── __init__.cpython-311.pyc
│   │       │   └── routes.cpython-311.pyc
│   │       ├── routes.py
│   │       └── templates
│   │           ├── generate_document.html
│   │           └── index.html
│   ├── static
│   │   ├── css
│   │   │   └── main.css
│   │   └── js
│   │       ├── theme-init.js
│   │       └── theme-toggle.js
│   ├── templates
│   │   ├── base.html
│   │   └── components
│   │       ├── footer.html
│   │       └── navbar.html
│   └── utils
│       ├── __pycache__
│       │   └── mock_data.cpython-311.pyc
│       └── mock_data.py
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
├── run.py
└── tests
    ├── __pycache__
    │   ├── __init__.cpython-310.pyc
    │   ├── __init__.cpython-311.pyc
    │   ├── conftest.cpython-311-pytest-9.0.1.pyc
    │   ├── test_auth.cpython-311-pytest-9.0.1.pyc
    │   ├── test_base_routes.cpython-311-pytest-9.0.1.pyc
    │   ├── test_coverage.cpython-311-pytest-9.0.1.pyc
    │   ├── test_dashboard.cpython-311-pytest-9.0.1.pyc
    │   └── test_debug_routes.cpython-311-pytest-9.0.1.pyc
    ├── conftest.py
    ├── test_auth.py
    ├── test_base_routes.py
    ├── test_coverage.py
    └── test_dashboard.py
```


## 🛠️ Configuración Local

### Prerrequisitos
- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

```bash
# 1. Clonar el repositorio
git clone <tu-repositorio>
cd saas-frontend

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
# venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
python run.py

# 6. Acceder en el navegador
# http://localhost:5000
```

## 🐳 Ejecución con Docker

```bash
# Construir y levantar los contenedores
docker-compose up --build

# La aplicación estará disponible en:
# http://localhost:5000

# Para detener los contenedores
docker-compose down
```

## 🧪 Pruebas

El proyecto incluye una suite de pruebas automatizadas:

```bash 
# Ejecutar todas las pruebas
pytest

# Ejecutar pruebas específicas
pytest tests/test_auth.py
pytest tests/test_dashboard.py

# Con reporte detallado
pytest -v
```
