from django.test import Client, TestCase

class ReceiptTestCases(TestCase):
    def test_right_file_type(self):
        with open('./receipt_processor/tests_files/sample.txt') as fp:
            c = Client()
            response = c.post('/receipts/', {'receipt_doc': fp})
            self.assertEqual(c.status_code, 200)

    def test_wrong_file_type(self):
        with open('./receipt_processor/tests_files/sample.pdf') as fp:
            c = Client()
            response = c.post('/receipts/', {'receipt_doc': fp})
            self.assertEqual(c.status_code, 400) 
            self.assertEqual(c.content, { 'errors': ['Invalid File Type']}) 
