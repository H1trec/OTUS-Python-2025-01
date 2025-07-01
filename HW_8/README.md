### Django ORM

В каталоге находятся все файлы проекта приложения Store.

Результат мирации:
```
(.venv) PS C:\Users\User\PycharmProjects\DjangoProject> python manage.py makemigrations
Migrations for 'store':
  store\migrations\0001_initial.py
    + Create model Category
    + Create model Product
(.venv) PS C:\Users\User\PycharmProjects\DjangoProject> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, store
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
  Applying store.0001_initial... OK

```
Результат создания данных:
```
(.venv) PS C:\Users\User\PycharmProjects\DjangoProject> python manage.py create_data
Test data created successfully!
(.venv) PS C:\Users\User\PycharmProjects\DjangoProject> python manage.py shell
8 objects imported automatically (use -v 2 for details).
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from store.models import Category, Product
>>> Category.objects.all()
<QuerySet [<Category: Electronics>, <Category: Furniture>]>
>>> Product.objects.all()
<QuerySet [<Product: Laptop (Electronics)>, <Product: Chair (Furniture)>]>
```

Создал пользователя с правами superuser:
```
(.venv) PS C:\Users\User\PycharmProjects\DjangoProject> python manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: admin@mail.ru
Password:
Password (again):
Superuser created successfully.
```
