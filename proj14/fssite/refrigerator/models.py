from django.conf import settings
from django.db import models

# Create your models here.
class FoodCategory(models.Model):
    """ 食品のカテゴリー """
    name = models.CharField(help_text="食品を分類する名前", max_length=256)

class Food(models.Model):
    """ 食品 """
    category = models.ForeignKey(FoodCategory, help_text="食品のカテゴリー")
    name = models.CharField(help_text="食品自体の名前", max_length=256)

class Stock(models.Model):
    """ 冷蔵庫に今入っている在庫"""
    food = models.ForeignKey(Food, help_text="冷蔵庫に入っている食品の種類")
    pub_by = models.ForeignKey(settings.AUTH_USER_MODEL, help_text="この在庫を入れた人")
    amount = models.PositiveSmallIntegerField(help_text="この在庫の個数")
    expiration_date = models.DateField(help_text="この在庫が消費期限切れになってしまう日付")
