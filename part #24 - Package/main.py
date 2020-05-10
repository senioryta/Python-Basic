'''

import sound.animals
import sound.transport

sound.animals.dog(3)
sound.transport.car(2)

--------------------------

from sound import animals
from sound import transport

animals.bird(5)
transport.motorcycle(2)

-------------------------

from sound import animals as an
from sound import transport as tr

an.cow(4)
tr.motorcycle(33)

---------------------------

import sound

sound.cow(1)
sound.car(4)

----------------------------
'''

from sound import *

cow(3)
motorcycle(2)
horse(6)