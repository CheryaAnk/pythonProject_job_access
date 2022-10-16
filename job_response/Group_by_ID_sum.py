# Словарь, где ключом будет номер группы(сумма цифр ID), значением - число покупателей с этим номером группы.
group_dict = {}


# Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная
# и начинается с 0. На вход функция получает целое число n_customers (количество клиентов).
def groups_id_from_zero(n_customers: int) -> dict[int, int]:
    for cur_id in range(0, n_customers):
        # Найдем сумму цифр текущего ID
        group_name = sum([int(i) for i in str(cur_id)])
        # Проитерируем счетчик покупателей в нашем словаре или создадим новый ключ с дефолтом 0
        group_count = group_dict.setdefault(group_name, 0) + 1
        group_dict[group_name] = group_count
    return group_dict


# Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если ID начинается с
# произвольного числа. На вход функция получает целые числа: n_customers (количество клиентов) и
# n_first_id (первый ID в последовательности).
def groups_id_from_number(n_customers: int, n_first_id: int) -> dict[int, int]:
    for cur_id in range(n_first_id, n_first_id + n_customers):
        group_name = sum([int(i) for i in str(cur_id)])
        group_count = group_dict.setdefault(group_name, 0) + 1
        group_dict[group_name] = group_count
    return group_dict
