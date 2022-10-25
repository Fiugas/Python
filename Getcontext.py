from decimal import getcontext
from decimal import Decimal

ctx = getcontext()
num = Decimal('1.1') 
print(num**4)
ctx.prec = 2
print(num**4)