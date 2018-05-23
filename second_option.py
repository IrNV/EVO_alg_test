from first_option import generate_servers, generate_mirror
from copy import deepcopy
import sys


def translate_servers(servers):
    """
    Переводим список в последовтельность битов, где значения списка это позиции битов
    имеющих значени 1, например, [1, 2, 4] -> 0b1011
    :param servers: список серверов [[...], [...], ...]
    :return: список серверов представленных последовательностью бит
    """
    array = []

    for index, server in enumerate(servers):
        bits_array = 0b0
        for replica in server:
            bits_array |= 0b1 << (replica - 1)

        array.append(bits_array)

    return array


def calculate_probability_failure(servers):
    """
    :param servers: список серверов представленных последовательностью бит
    :param n: кол-во серверов
    :return: словарь: ключ - № сервера, значение - вероятность потери данных
    """
    # Словарь: хранящий ключ - № сервера,
    # значение - вероятность потери данных при падении сервера
    server_count = len(servers)
    chances = {}
    for i in range(server_count):
        chances[i] = 0
    loose_chance = 100 / (server_count - 1)  # шанс потери данных, если сервер падает (в нашем случае все равны)

    data = deepcopy(servers)  # делаем копию входных данных, что бы не изменить входные данные в процессе обработки

    for index in range(server_count - 1):
        next_server = index

        while data[index] != 0:
            next_server += 1

            # Операцией "И" получаем битовую последовательность, где 1 стоят на позициях
            # в которых и в первой и в второй последовательностях стоят 1.
            result = data[index] & data[next_server]
            if result != 0:
                # наличие единичных битов в одинаковых позициях означает, что сервера
                # имеют одинаковые реплики данных. Поэтому добавляем вероятность потери.
                chances[index] += loose_chance
                chances[next_server] += loose_chance
                # обнуляем совпавшие биты
                data[index] = data[index] & (~ result)
                data[next_server] = data[next_server] & (~ result)

    return chances


if __name__ == "__main__":
    if sys.argv[3] in ["--random", "--mirror"]:
        if sys.argv[3] == "--random":
            servers = generate_servers(int(sys.argv[2]))
            servers = translate_servers(servers)
        elif sys.argv[3] == "--mirror":
            if int(sys.argv[2]) % 2 != 0:
                print("Wrong n for mirror! n can be k * 2 (2, 4, 6 ...)")
                exit()
            servers = generate_mirror(int(sys.argv[2]))
            servers = translate_servers(servers)

        result = calculate_probability_failure(servers)
        for key in result:
            print("Killing {} arbitrary servers results in data loss in {}% cases".format(key + 1,
                                                                                          round(result[key]), 2))
