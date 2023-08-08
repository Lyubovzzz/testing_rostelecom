Необходимо протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии. 

→ Объект тестирования: https://b2c.passport.rt.ru

Заказчик передалследующее задание:

1.Протестировать требования.
2.Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
3.Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс.


Ожидаемый результат:

1. Перечислены инструменты, которые применялись для тестирования:

Почему именно этот инструмент и эту технику?
Что им проверялось?

К выполненному заданию прикреплены:

1.Набор тест-кейсов.
2.Набор автотестов на GitHub. 
3.Описание оформленных дефектов.

________________________________________

Каталог проекта содержит файлы:

config.py - хранит переменные, используемые в проекте;
requirements.txt - содержит библиотеки и зависимости

________________________________________

Директория chromedriver-win64 содержит:

chromedriver.exe - драйвер для запуска и управления браузером Chrome

________________________________________

Директория tests содержит:

conftest.py - хранит фикстуры для запуска тестов;
locators.py - содержиткласс локаторов с описанием;
test_rostelecom.py - содержит тесты 

________________________________________

Директория manual_testing содержит:

test_cases - тест кейсы , составленные в соотвествии с требованиями
test_docunentation - протестированная документация
