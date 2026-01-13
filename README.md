# 📚 Bookstore Inventory API - Nextep Innovation

API REST robusta diseñada para la gestión de inventario de una cadena de librerías, con integración de tasas de cambio en tiempo real y cálculo automatizado de precios de venta sugeridos[cite: 4, 5].

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