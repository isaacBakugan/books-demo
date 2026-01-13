import requests
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from django.db import connection
import os

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'], url_path='calculate-price')
    def calculate_price(self, request, pk=None):
        book = self.get_object()
        try:
            # Integración externa 
            response = requests.get(os.environ.get('EXCHANGE_RATE_API_URL'), timeout=5)
            rate = response.json()['rates'].get('EUR', 0.85) # Tasa por defecto si falla 
            currency = "EUR"
        except:
            rate = 0.85
            currency = "EUR"

        # Matemática de negocio: 40% de margen 
        cost_local = float(book.cost_usd) * rate
        selling_price = cost_local * 1.40 
        
        book.selling_price_local = selling_price
        book.save() # Persistencia 
        return Response({
            "book_id": book.id,
            "cost_usd": book.cost_usd,
            "exchange_rate": rate,
            "cost_local": round(cost_local, 2),
            "margin_percentage": 40,
            "selling_price_local": round(selling_price, 2),
            "currency": currency,
            "calculation_timestamp": timezone.now()
        })
    def get_queryset(self):
        queryset = Book.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__icontains=category)
        return queryset

    # 2. Libros con stock bajo
    @action(detail=False, methods=['get'], url_path='low-stock')
    def low_stock(self, request):
        threshold = request.query_params.get('threshold', 10)
        books = Book.objects.filter(stock_quantity__lte=threshold)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
    
def health_check(request):
    """
    Endpoint para que Cloud Run y Nextep sepan que no hemos incendiado el servidor.
    """
    health_data = {
        "status": "ok",
        "database": "connected",
        "timestamp": "2026-01-12T..." # ¡Recuerda que ya estamos en el 2026!
    }
    try:
        # Verificamos si la base de datos de Supabase nos sigue queriendo
        print("test")
        connection.ensure_connection()
    except Exception as e:
        health_data["status"] = "unhealthy"
        health_data["database"] = f"error: {str(e)}"
        return JsonResponse(health_data, status=503) # Service Unavailable 

    return JsonResponse(health_data)

    