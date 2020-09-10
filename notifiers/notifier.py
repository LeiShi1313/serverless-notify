import httpx
from fastapi import APIRouter

from utils import camel_case_to_snake_case

router = APIRouter()

class NotifierMount(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'notifiers'):
            cls.notifiers = {}
        else:
            cls.register_notifier(cls)
    
    def register_notifier(cls, notifier):
        instance = notifier()
        name = camel_case_to_snake_case(instance.__class__.__name__)
        cls.notifiers[name] = instance
        router.get(f"/{name}")(instance.notify)
        

class Notifier(metaclass=NotifierMount):
    pass





