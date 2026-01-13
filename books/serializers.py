from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # Campo calculado que no está en la DB pero queremos mostrar
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'isbn', 
            'cost_usd', 'selling_price_local', 
            'stock_quantity', 'category', 'supplier_country'
        ]
        read_only_fields = ['selling_price_local'] # Solo lo toca nuestra lógica