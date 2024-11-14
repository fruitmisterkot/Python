# TODO решите задачу
import json
INPUT_FILENAME = "input.json"
def task() -> float:
    sum = 0
    with open(INPUT_FILE, 'r') as file:
        file_obj = json.load(file)
        for data in file_obj:
            score = data["score"]
            weight = data["weight"]
            sum += score * weight
    return round(sum, 3)


print(task())
