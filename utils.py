import re

def camel_case_to_snake_case(name: str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()