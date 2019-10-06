import hashlib
import random

def get_ticket():
    x = random.randint(1000, 20000)
    x= str(x)
    result = hashlib.sha1(x.encode())
    return  result.hexdigest()