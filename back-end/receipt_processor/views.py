from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from receipt_processor.models import Receipt
from receipt_processor.serializers import ReceiptSerializer
from receipt_processor.interactors.receipt_processor import process

import logging
logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def receipt_list(request, format=None):
    if request.method == 'GET':
        receipts = Receipt.objects.all()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = process(request)
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({ 'errors': ['Invalid File Type']}, status=status.HTTP_400_BAD_REQUEST)