import unittest
from first_algorithm import calculate_probability_failure
import second_algorithm

data1 = [[1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [11, 12, 13, 14, 15]]

data2 = [[1, 4, 7, 12, 15],
         [1, 5, 8, 12, 13],
         [2, 5, 7, 11, 14],
         [2, 6, 8, 10, 15],
         [3, 6, 9, 11, 13],
         [3, 4, 9, 10, 14]]


class CalcTests(unittest.TestCase):
    def test_mirror_first_option_probability_calc(self):
        """
         Проверяем первый вариант алгоритма на зеркальных данных из задания
        """
        result = calculate_probability_failure(data1)
        self.assertEqual(result[0], 20)

    def test_rand_first_option_probability_calc(self):
        """
         Проверяем первый вариант алгоритма на случайных данных из задания
        """
        result = calculate_probability_failure(data2)
        self.assertEqual(result[0], 80)

    def test_mirror_second_option_probability_calc(self):
        """
         Проверяем второй вариант алгоритма (переводом серверов в последовательность бит)
          на зеркальных данных из задания
        """
        translated = second_algorithm.translate_servers(data1)
        result = second_algorithm.calculate_probability_failure(translated)
        self.assertEqual(result[0], 20)

    def test_rand_second_option_probability_calc(self):
        """
         Проверяем второй вариант алгоритма (переводом серверов в последовательность бит)
          на случайных данных из задания
        """
        translated = second_algorithm.translate_servers(data2)
        result = second_algorithm.calculate_probability_failure(translated)
        self.assertEqual(result[0], 80)


if __name__ == '__main__':
    unittest.main()
