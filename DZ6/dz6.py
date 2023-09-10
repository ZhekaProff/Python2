# Задача 1
a = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))
# Создаем пустой массив
progression = []
# Заполняем массив элементами арифметической прогрессии
for i in range(n):
    progression.append(a + i * d)
print("Массив элементов арифметической прогрессии:", progression)


# Задача2
def find_indexes(arr, min_value, max_value):
    indexes = []
    for i in range(len(arr)):
        if arr[i] >= min_value and arr[i] <= max_value:
            indexes.append(i)
    return indexes


# Пример использования:
array = [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]

minimum = 3
maximum = 7
result = find_indexes(array, minimum, maximum)
print(result)
