from rest_framework import serializers
from receipt_processor.models import Receipt, Block

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'begin_row', 'begin_col', 'end_row', 'end_col']

class ReceiptSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True, read_only=True)

    class Meta:
        model = Receipt
        fields = ['id', 'receipt_doc', 'blocks']
    
    