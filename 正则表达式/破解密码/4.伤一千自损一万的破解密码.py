import time
import itertools
import itertools
#mylist = list(itertools.product("1234567890",repeat=5))

passwd = ("".join(x) for x in itertools.product("1234567890",repeat=10))
#print(len(mylist))

while True:
    try:
        time.sleep(0.1)
        str = next(passwd)
        print(str)
    except StopIteration as e :
        break