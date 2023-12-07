# TODO решите задачу
import json

FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)
    sumproduct = sum([value["score"]*value["weight"] for value in data])
    return round(sumproduct, 3)


print(task())
