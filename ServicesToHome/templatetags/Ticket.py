import hashlib
import random
from django import template

register = template.Library()
@register.simple_tag
def get_ticket():
    x = random.randint(1000, 20000)
    x = str(x)
    result = hashlib.md5(x.encode())
    return result.hexdigest()