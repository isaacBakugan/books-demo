from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

class Book(models.Model):
    # ISBN 10 o 13 dígitos y único 
    isbn_validator = RegexValidator(regex=r'^\d{10}(\d{3})?$', message="ISBN inválido.")
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True, validators=[isbn_validator])
    
    # Costo > 0 
    cost_usd = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    selling_price_local = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    
    # Stock no negativo 
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.CharField(max_length=100)
    supplier_country = models.CharField(max_length=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)