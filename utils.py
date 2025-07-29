import re


def pascal_to_kebab(s:str):
    return re.sub(r'(?<!^)(?=[A-Z])', '-', s).lower()
