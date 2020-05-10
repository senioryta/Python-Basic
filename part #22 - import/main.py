'''

import fibonacci

fibonacci.fib(1000)
print(fibonacci.fib2(1000))

---------------------------

import fibonacci as fibo

fibo.fib(1000)
fibo.fib2(1000)

---------------------------

from fibonacci import fib
from fibonacci import fib2

fib(1000)
print(fib2(1000))

----------------------------

from fibonacci import fib as f
from fibonacci import fib2 as f2

f(1000)
f2(1000)

'''

from fibonacci import *

fib(1000)
print(fib2(1000))