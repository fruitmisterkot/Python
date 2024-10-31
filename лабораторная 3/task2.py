# TODO Напишите функцию find_common_participants
def find_common_participants(string1, string2, splitter=","):
    spl_string1 = string1.split(splitter)
    spl_string2 = string2.split(splitter)
    set_one = set(spl_string1)
    set_two = set(spl_string2)
    intersection = set_one.intersection(set_two)
    list_intersection = list(intersection)
    list_intersection.sort()
    return list_intersection

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

interseption = find_common_participants(participants_first_group, participants_second_group, "|")
print(interseption)