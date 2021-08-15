import re
from receipt_processor.models import Receipt, Block
from receipt_processor.serializers import ReceiptSerializer

def process (request):
    if request.FILES['receipt_doc'].content_type == 'text/plain':
        newdoc = Receipt.objects.create(receipt_doc=request.FILES['receipt_doc'])
        newdoc.save()
        
        l = []
        sc = ec = sr = er = None    

        with open(newdoc.receipt_doc.name, 'r') as reader:
            for index, line in enumerate(reader.readlines()):
                s = list(re.finditer('\S+', line))
                if s and not (len(s[0].group(0)) >= 5 and len(set(s[0].group(0))) == 1):
                    if sr == None:
                        sr = index
                    if not sc or s[0].span()[0] < sc:
                        sc = s[0].span()[0]
                    if not ec or s[-1].span()[1] > ec:
                        ec = s[-1].span()[1]
                elif sc != None:
                    er = index
                    l.append(Block(begin_row=sr, begin_col=sc, end_row=er, end_col=ec, receipt=newdoc))
                    sc = ec = sr = er = None
            else:
                if sc:
                    er = index + 1
                    l.append(Block(begin_row=sr, begin_col=sc, end_row=er, end_col=ec, receipt=newdoc))
                    sc = ec = sr = er = None

        Block.objects.bulk_create(l)
        return ReceiptSerializer(instance=newdoc)
    return False