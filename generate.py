from jinja2 import Environment, FileSystemLoader
from models import Model
from utils import pascal_to_kebab


import json
import argparse
import pyperclip


parser = argparse.ArgumentParser()
available_models = {}
for klass in Model.__subclasses__():
    available_models[pascal_to_kebab(klass.__qualname__)] = klass

parser.add_argument("modelname", choices=available_models.keys())

for klass in Model.__subclasses__():
    for parameter, type in klass.parameters.items():
        parser.add_argument(f"--{parameter}", type=type, required=False)

parser_args = parser.parse_args()
model = available_models[parser_args.modelname]

env = Environment(loader=FileSystemLoader("templates/"))
template = env.get_template(model.template)
extra_context = {}

for parameter, type in model.parameters.items():
    extra_context[parameter] = getattr(parser_args, parameter)

with open(f"context/{model.context}") as file:
    context = json.load(file)
    context.update(extra_context)
    rendered = template.render(context)

    pyperclip.copy(rendered)
    print("Copied to clipboard!")
