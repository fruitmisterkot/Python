# TODO решите задачу
import json
INPUT_FILENAME = "input.json"
def task() -> float:
    with open(INPUT_FILENAME, 'r') as file:
        file_obj = json.load(file)
        list_multiply = [data["score"] * data["weight"] for data in file_obj]
        summar = sum(list_multiply)
    return round(summar, 3)


print(task())
