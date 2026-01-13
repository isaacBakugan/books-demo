from django.contrib import admin
from django.urls import path, include
from .views import health_check # Importa tu nueva creación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check), # El endpoint de vida o muerte
    path('api/', include('books.urls')), # Donde vivirá el CRUD y el cálculo [cite: 35-45]
]