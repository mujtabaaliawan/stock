from django.db import models
from stock_detail.models import StockDetail
from trader.models import Trader


class Transaction(models.Model):
    nature_choices = [
        ("purchase", "purchase"),
        ("sale", "sale")
    ]
    nature = models.CharField(max_length=10, choices=nature_choices, default="purchase")
    date_time = models.DateTimeField(auto_now_add=True)
    volume_transacted = models.IntegerField()
    stock_detail = models.ForeignKey(StockDetail, on_delete=models.CASCADE, related_name='transaction_stock')
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, related_name='transaction_trader')



