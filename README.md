Данный репозиторий содержит проект тестового задания для EVO.
Дано: сервера с репликами, всего по 2 копии реплик, которые не могут находится на одном сервере.
Найти веройтность потери данных при падении серверов.

Файл first_option содержит функции генераторы серверов с случайными репликами, а так же стандартный алгоритм, который просматривает есть ли на оставшихся серверах реплики из упавшего сервера и считает вероятность потери данных.
Файд second_option содержит 2-й вариант алгоритма, в котором сервера представлены как последовательность бит и обрабатываются с помощью битовых операций.


Версия python - 3.6