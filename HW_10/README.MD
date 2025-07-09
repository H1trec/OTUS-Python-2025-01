### Class-Based Views и тестирование

Проект был доработан добавлением Class-Based Views и функцией удаления товаров.


Тесты:
```
(.venv) PS C:\Users\User\PycharmProjects\DjangoProject> pytest store/tests/test_models.py -v
======================================================================================================= test session starts =======================================================================================================
platform win32 -- Python 3.12.0, pytest-8.4.1, pluggy-1.6.0 -- C:\Users\User\PycharmProjects\DjangoProject\.venv\Scripts\python.exe
cachedir: .pytest_cache
django: version: 5.2.3, settings: DjangoProject.settings (from option)
rootdir: C:\Users\User\PycharmProjects\DjangoProject\store
configfile: pytest.ini
plugins: django-4.11.1
collected 4 items                                                                                                                                                                                                                   

store\tests\test_models.py::test_product_creation PASSED                                                                                                                                                                     [ 25%] 
store\tests\test_models.py::test_product_update PASSED                                                                                                                                                                       [ 50%] 
store\tests\test_models.py::test_product_deletion PASSED                                                                                                                                                                     [ 75%] 
store\tests\test_models.py::test_price_validation PASSED                                                                                                                                                                     [100%] 

======================================================================================================== 4 passed in 1.86s ======================================================================================================== 
```
