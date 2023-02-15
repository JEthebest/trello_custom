from django.db import models

from django.contrib.auth.models import User

from board.models import Task

# Create your models here.

class OrderCard(models.Model):
    full_name = models.CharField(max_length=300, verbose_name="Полное имя")
    number = models.CharField(max_length=20, verbose_name="Номер")
    product_url = models.URLField(max_length=20, default='https://default.com', verbose_name="Ссылка продукта")
    product_amount = models.PositiveIntegerField(default=1, verbose_name="Количество продукта")
    price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Цена")
    invoice = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Счет")
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name="Адрес")
    work = models.CharField(max_length=200, blank=True, null=True, verbose_name="Работа")
    delivery_report = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Aкт о доставке")
    period = models.IntegerField(verbose_name="Период")
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Создатель")
    # vendor = models.ForeignKey(Vendor, related_name='orders', on_delete=models.CASCADE, verbose_name="Поставщик")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано в")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обнавлено в")
    # area = models.ForeignKey(Area, default=None, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Область")
    # objects = OrderCardManager()
    order_code = models.CharField(max_length=5, blank=True, null=True, verbose_name="Код заказа")
    # bank_branch = models.ForeignKey("profiles.BankBranch", on_delete=models.CASCADE, verbose_name="Банковский филиал")

    # client passport data
    passport_front = models.ImageField(upload_to='images', null=True, blank=True, verbose_name="Паспорт фронтальный")
    passport_back = models.ImageField(upload_to='images', null=True, blank=True, verbose_name="Паспорт зад")
    passport_number = models.CharField(max_length=300, null=True, blank=True, verbose_name="Номер паспорта")
    passport_inn = models.CharField(max_length=300, null=True, blank=True, verbose_name="ИНН")
    passport_issued_by = models.CharField(max_length=300, null=True, blank=True, verbose_name="Выдан")
    passport_issued_date = models.DateField(null=True, blank=True, verbose_name="Дата выдачи")

    board = models.OneToOneField(Task, on_delete=models.CASCADE)
    
    #credit data
    disposal = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Распоряжение")
    request_data = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Запрос")