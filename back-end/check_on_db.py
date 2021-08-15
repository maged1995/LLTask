import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'receipt_system.settings'
from django.db import connections

print('########### DB Check start ###########')

with connections['postgres'].cursor() as cursor:
    try:
        cursor.execute("SELECT datname FROM pg_database where datname = 'mydatabase';")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute('CREATE DATABASE mydatabase;')
    except:
        cursor.execute('CREATE DATABASE mydatabase;')

print('########### DB Check end ###########')