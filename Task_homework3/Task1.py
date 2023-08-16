# Дан список повторяющихся элементов 
# Вернуть список с дублирующимися элементами 
# В результирующем списке не должно быть дубликатов


def double_list(array: list[int]) -> list[int]:
    res = set()
    for el in array:
        counter = array.count(el)
        if counter > 1:
            res.add(el)
    return list(res)
print(double_list([10, 14, 25, 36, 10, 25, 78, 16, 96, 14]))