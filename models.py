from typing import Any


class Model:
    template: str
    output: str
    context: str
    parameters: dict[str,Any]

class CrystalAssembler(Model):
    template = "crystal.jinja.sfm"
    output = "crystal.sfm"
    context = "crystal.json"
    parameters = {
        "machineCount": int
    }
