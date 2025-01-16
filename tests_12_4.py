import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = Runner('Петя', -15)      # отрицательная скорость
            runner_1.walk()
            self.assertEqual(runner_1.distance, 50)                                   # проверка на условия
            logging.info(f'"test_walk" выполнен успешно', exc_info=True)                # сообщение при выполнении
        except ValueError:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)             # сообщение при ошибке


    def test_run(self):
        try:
            runner_2 = Runner(50)                     # отсутствует имя
            runner_2.run()
            self.assertEqual(runner_2.distance, 100)                                  # проверка на условия
            logging.info(f'"test_walk" выполнен успешно', exc_info=True)                # сообщение при выполнении
        except TypeError:
            logging.warning(f"Неверный тип данных для объекта Runner", exc_info=True)   # сообщение при ошибке





if __name__ == '__main__':
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")  # настройка basicConfig