# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as input_data:
        lines = [line for line in csv.DictReader(input_data)]
        with open(OUTPUT_FILENAME, 'w') as out_data:
            json.dump(lines, out_data, indent=4)







if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
