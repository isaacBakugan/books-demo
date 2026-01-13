# 📚 Bookstore Inventory API - Nextep Innovation

API REST robusta diseñada para la gestión de inventario de una cadena de librerías, con integración de tasas de cambio en tiempo real y cálculo automatizado de precios de venta sugeridos.

## 🛠️ Tech Stack
* **Lenguaje:** Python 3.9
* **Framework:** Django 4.2.27 (LTS) & Django Rest Framework
* **Base de Datos:** PostgreSQL (Hosted on Supabase/GCP)
* **Contenedores:** Docker & Docker Compose 
* **Integración:** ExchangeRate API (USD to Local Currency) [cite: 47]

## 🚀 Requerimientos Previos
* Docker y Docker Compose instalados.
* Git para clonación del repositorio.
* Archivo `.env` configurado (ver sección de variables).

## 📥 Instalación y Ejecución Local
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/isaacBakugan/books-demo.git
   cd bookstore_inventory_api 

2. Levantar el entorno
   docker-compose up --build

📡 Endpoints de la API
Base URLs
Producción: https://bookstore-api-858025381397.us-central1.run.app/

Local: http://localhost:8000/

Cómo probar con la Colección de Postman
He incluido el archivo BOOK-lGCP.postman_collection.json. Para usarlo:

Importa el archivo en Postman.

Para cambiar entre Local y Nube:

Simplemente edita la URL base en la colección de https://bookstore-api... a http://localhost:8000