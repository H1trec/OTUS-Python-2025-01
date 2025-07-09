### Class-Based Views и тестирование

Проект был доработан добавлением Class-Based Views и функцией удаления товаров.
Список товаров:   
![LIST](https://github.com/H1trec/H1trec-OTUS-NoSQL-2025-01/blob/main/OTUS-Python-2025-01/list.JPG?raw=true)
Редактирование товара:   
![EDIT](https://github.com/H1trec/H1trec-OTUS-NoSQL-2025-01/blob/main/OTUS-Python-2025-01/edit.JPG?raw=true)
![RESULT_EDIT](https://github.com/H1trec/H1trec-OTUS-NoSQL-2025-01/blob/main/OTUS-Python-2025-01/result.JPG?raw=true)
Удаление товара:    
![DELETE](https://github.com/H1trec/H1trec-OTUS-NoSQL-2025-01/blob/main/OTUS-Python-2025-01/del.JPG?raw=true)
![RESULT_DELETE](https://github.com/H1trec/H1trec-OTUS-NoSQL-2025-01/blob/main/OTUS-Python-2025-01/resultdel.JPG?raw=true)

Добвление товара:   
![ADD](https://github.com/H1trec/H1trec-OTUS-NoSQL-2025-01/blob/main/OTUS-Python-2025-01/add.JPG?raw=true)
![RESULT_ADD](https://github.com/H1trec/H1trec-OTUS-NoSQL-2025-01/blob/main/OTUS-Python-2025-01/resultadd.JPG?raw=true)

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
