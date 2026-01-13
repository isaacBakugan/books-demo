from django.contrib import admin
from django.urls import path, include
from books.views import health_check # Importas tu función

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check), # La ruta que estamos probando
    path('api/books/', include('books.urls')), # ¡Aquí es donde fallaría si falta el archivo!
]