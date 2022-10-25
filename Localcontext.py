from decimal import getcontext
from decimal import Decimal
from decimal import localcontext 

ctx = getcontext()
num = Decimal('1.1') 
print(num**4)
with localcontext() as local_cntx:
    local_cntx.prec = 2
    print(num**4)