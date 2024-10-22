numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

index_imposter = numbers.index(None)
numbers_left = numbers[:index_imposter]
numbers_right = numbers[index_imposter + 1:]
new_numbers = numbers_right + numbers_left
sredn = sum (new_numbers)/ len(numbers)
numbers[index_imposter] = sredn
print("Измененный список:", numbers)