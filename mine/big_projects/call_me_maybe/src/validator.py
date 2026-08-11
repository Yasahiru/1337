from models import FunctionDefinition, ParameterDefinition, ReturnDefinition, Prompt
import json
import sys


class Validator:
    def __init__(self):
        self.functions_obj = []
        self.prompts = []


    def load_functions(self, file: str) -> None:
        with open(file, mode="r") as f:
            data = json.load(f)

        for fun in data:
            params = {}

            for k, v in fun["parameters"].items():
                params[k] = ParameterDefinition(type=v["type"])

            ret = ReturnDefinition(type=fun["returns"]["type"])

            function = FunctionDefinition(
                name=fun["name"],
                description=fun["description"],
                parameters=dict(params),
                returns=ret
            )
            self.functions_obj.append(function)

    def load_prompts(self, file: str) -> None:
        with open(file, mode="r") as f:
            data = json.load(f)

        for line in data:
            self.prompts.append(
                Prompt(prompt=line["prompt"])
            )


if __name__ == "__main__":
    try:
        v = Validator()
        v.load_functions("data/input/functions_definition.json")
        v.load_prompts("data/input/function_calling_tests.json")

        for el in v.functions_obj:
            print(el.name)
        print()
        for p in v.prompts:
            print(p)
    except KeyboardInterrupt as e:
        print(e)
