from django.db import models

class ClothingItem(models.Model):
    CATEGORY_CHOICES = [
        ('man', 'Чоловічий'),
        ('woman', 'Жіночий'),
        ('kids', 'Дитячий'),
    ]

    name = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    size = models.CharField(max_length=10, verbose_name="Розмір")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name="Категорія")
    available = models.BooleanField(default=True, verbose_name="В наявності")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    def str(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Ім'я покупця")
    customer_email = models.EmailField(verbose_name="Email")
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")

    def str(self):
        return f"Замовлення #{self.id} — {self.customer_name}"
