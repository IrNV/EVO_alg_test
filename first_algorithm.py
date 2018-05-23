"""
Первый вариант алгоритма.
"""
from server_generator import generate_mirror, generate_servers
import sys


def calculate_probability_failure(servers):
    """
    :param servers: список серверов
    :return: словарь: ключ - № сервера, значение - вероятность потери данных
    """
    server_count = len(servers)  # количество серверов
    loose_chance = 100 / (server_count - 1)  # шанс потери данных, если сервер падает
    chances = {}
    for i in range(server_count):
        chances[i] = 0

    # проходим с первого до предпоследнего (включительно) сервера сравниваем его реплики
    # c последующими за ним серверами, если есть совпадения, то добавляем вероятность потери
    for first in range(server_count - 1):
        for second in range(first + 1, server_count):
            for i in servers[first]:
                if i in servers[second]:
                    chances[first] += loose_chance
                    chances[second] += loose_chance
                    break

    return chances


if __name__ == "__main__":
    if sys.argv[3] in ["--random", "--mirror"]:
        if sys.argv[3] == "--random":
            servers = generate_servers(int(sys.argv[2]))
        elif sys.argv[3] == "--mirror":
            if int(sys.argv[2]) % 2 != 0:
                print("Wrong n for mirror! n can be k * 2 (2, 4, 6 ...)")
                exit()
            servers = generate_mirror(int(sys.argv[2]))

        result = calculate_probability_failure(servers)
        for key in result:
            print("Killing {} arbitrary servers results in data loss in {}% cases".format(key + 1,
                                                                                          round(result[key], 2)))
