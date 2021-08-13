from django.db import models

class Receipt(models.Model):
    receipt_doc = models.FileField(upload_to='uploads/receipts/', default='', blank=True)

    
class Block(models.Model):
    begin_row = models.IntegerField()
    begin_col = models.IntegerField()
    end_row = models.IntegerField()
    end_col = models.IntegerField()
    receipt = models.ForeignKey(Receipt, related_name='blocks', on_delete=models.CASCADE)
    class Meta:
        unique_together = ['receipt']