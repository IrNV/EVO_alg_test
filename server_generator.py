import random


def random_paired_servers(numbers_list, server_count):
    """
    Функция сортировки в случае парного кол-ва серверов
    :param numbers_list: список реплик
    :param server_count: кол-во серверов
    :return: сервера с репликами
    """
    # Случайным образом заполняем первую половину серверов, а затем вторую и соединяем их
    random.shuffle(numbers_list)
    left_part = numbers_list
    numbers_list = [i for i in range(1, server_count ** 2 + 1)]
    random.shuffle(numbers_list)
    right_part = numbers_list

    return left_part + right_part


def random_unpaired_servers(numbers_list, server_count, s_size):
    """
    Функция сортировки в случае непарного кол-ва серверов
    :param numbers_list: список реплик
    :param server_count: кол-во серверов
    :param s_size: размер сервера
    :return: сервера с репликами
    """
    array = []
    random.shuffle(numbers_list)
    array += numbers_list

    # выделяем часть среднего сервера заполненого репликами первой части серверов
    part = array[s_size * (server_count // 2): s_size * (server_count // 2) + s_size // 2]

    # Дополняем средний сервер репликами из 2-й половины, которых нет в нем
    counter = 0
    for num in numbers_list:
        if num not in part:  # проверяем, что бы в средний "общий сервер" не было записано дупликата
            array.append(num)
            part.append(num)
            numbers_list.pop(numbers_list.index(num))
            counter += 1
        if counter == s_size: # проверяем есть ли место на сервере для реплик
            break
    array += numbers_list

    return array


def generate_servers(server_count):
    """
    Функция генерации серверов с репликами
    :param server_count: кол-во северов
    :return: сервара с репликами
    """
    s_size = 2 * server_count
    numbers_list = [i for i in range(1, server_count ** 2 + 1)]

    if server_count % 2 == 0:
        array = random_paired_servers(numbers_list, server_count)
    else:
        array = random_unpaired_servers(numbers_list, server_count, s_size)

    # сортируем реплики
    servers = []
    for i in range(server_count):
        servers.append(array[i * s_size: i * s_size + s_size])
        servers[i].sort()
    servers.sort()

    return servers


def generate_mirror(server_count):
    """
    Функция генерации симметричных серверов
    :param server_count: кол-во северов
    :return: сервара с репликами
    """
    array = []
    s_size = 2 * server_count
    numbers_list = [i for i in range(1, server_count ** 2 + 1)]
    if server_count % 2 == 0:
        random.shuffle(numbers_list)
        array = numbers_list + numbers_list

    servers = []
    for i in range(server_count):
        servers.append(array[i * s_size: i * s_size + s_size])
        servers[i].sort()
    servers.sort()

    return servers
