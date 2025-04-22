### Docker

#### Реализация

Проект как и требуется содержит  Dockerfile, с установкой зависимостей. Сам проект - файл main.py


#### Тест

Тест пройден успешно:
```
lisunov.andrey.y_dev@s00-0000-bi15:~/otus$ sudo  pytest /usr/src/otus/test_homework_05/test_app.py -s -vv
============================================================================================================ test session starts ============================================================================================================
platform linux -- Python 3.11.2, pytest-8.3.5, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /usr/src/otus/test_homework_05
plugins: Faker-37.1.0
collected 1 item

../../../usr/src/otus/test_homework_05/test_app.py::test_build_and_run_app Building in /usr/src/homework_05
running docker container detached
sending request to the image
PASSEDstopping docker container
docker container stopped

```
