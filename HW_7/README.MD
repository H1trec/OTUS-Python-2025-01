### Взаимодействие приложений между контейнерами, docker compose.


Файлы необходимые для развертывания приложения находятся в папке с ДЗ.   
Была создана модель "Библиотека", в которой 2 сущности: Читатели и Книги.   
Читатель имеет следующие аттритбуты:   
* ID(prymary_key)
* ФИО
* Дата рождения

Книга:   
* ID(prymary_key)
* ID Читателя(ссылка на читателя)
* Автор
* Дата, когда книгу взял читатель


#### Работа приложения

При первом запусек приложение создает и заполняет модель тестовыми данными, если в БД не найдены необходимые таблицы.

Главная страница:  

![main](https://github.com/H1trec/OTUS-Python-2025-01/blob/main/HW_7/screens/main.JPG?raw=true)


Страница читатели:   
![readers](https://github.com/H1trec/OTUS-Python-2025-01/blob/main/HW_7/screens/all_readers.JPG?raw=true)

Страница книги:   
![books](https://github.com/H1trec/OTUS-Python-2025-01/blob/main/HW_7/screens/all_books.JPG?raw=true)

Страница добавления читателя:   
![add_rearder](https://github.com/H1trec/OTUS-Python-2025-01/blob/main/HW_7/screens/add_user.JPG?raw=true)
Результат добавления:   
![add_rearder](https://github.com/H1trec/OTUS-Python-2025-01/blob/main/HW_7/screens/result_add_user.JPG?raw=true)

Страница добавления книги:    
![add_rearder](https://github.com/H1trec/OTUS-Python-2025-01/blob/main/HW_7/screens/add_book.JPG?raw=true)
Результат добавления:   
![add_rearder](https://github.com/H1trec/OTUS-Python-2025-01/blob/main/HW_7/screens/result_add_book.JPG?raw=true)

