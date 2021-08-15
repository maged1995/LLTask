from io import StringIO
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
import six

class ReceiptTestCases(TestCase):
    def test_right_file_type(self):
        with open('./receipt_processor/tests_files/sample.txt') as fp:
            response = self.client.post('/receipts/', {'receipt_doc': fp})
            self.assertEqual(response.status_code, 201)

    def test_wrong_file_type(self):
        pdf_file = StringIO('portable document format file')
        file = SimpleUploadedFile('test_file.pdf', content=six.b('bytes'), content_type='application/pdf')
        response = self.client.post('/receipts/', {'receipt_doc': file})
        self.assertEqual(response.status_code, 400) 
        self.assertJSONEqual(str(response.content, encoding='utf8'), { 'errors': ['Invalid File Type']} )