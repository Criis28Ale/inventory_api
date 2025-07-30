Inventory API – FastAPI

API REST sencilla para gestionar un inventario de productos, con operaciones CRUD básicas.

Cómo ejecutar localmente

1. Clona el repositorio:
bash
git clone https://github.com/tu_usuario/inventory-api.git
cd inventory-api

Instala las dependencias:
pip install -r requirements.txt

Endpoints principales
GET /items – Listar todos los productos.
POST /items – Crear un nuevo producto.
GET /items/{item_id} – Obtener un producto por ID.
PUT /items/{item_id} – Actualizar un producto.
DELETE /items/{item_id} – Eliminar un producto.

Ejecuta las pruebas automáticas con:
pytest

Usamos GitHub Actions para:
Instalar dependencias
Ejecutar lint con flake8
Ejecutar pruebas con pytest
Deploy automático en Render.com

https://inventory-api.onrender.com/

Tecnologías usadas
Python 3.10
FastAPI
Uvicorn
Pytest
Flake8
GitHub Actions
Render.com (hosting)
