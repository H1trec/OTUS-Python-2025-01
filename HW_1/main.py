import json
from collections import OrderedDict
#from curses.ascii import isdigit
#from http.cookiejar import uppercase_escaped_char

with open('phones.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    edit_flag = 0
while True:
    main_in = input("Выберите пункт меню для работы со справочником:\n 1- Показать все контакты\n 2- Найти контакт\n 3- Изменить контакт\n 4- Удалить контакт\n 5- Создать контакт\n 0- Выход из меню и окончание работы\n>>> ")
    def print_dict(dict):
        if not bool(dict):
            print('Данные отсутсвуют\n')
        for idx, name in dict.items():
            print(f'Контакт №{idx}')
            for key, value in name.items():
                print(f'\t{key:<8} {value}')
            print()


    def search_func(search_key, search_name):
        search_val = {k: v for k, v in data.items() if v.get(search_key).casefold() == search_name.casefold()}
        return search_val
    def update_func(update_key,update_type,update_val):
        data[update_key][update_type] = update_val

    try:
      menu_num = int(main_in)

      if menu_num == 0:
          if edit_flag == 0:
            print("Работа со спровочником завершена. Выход из программы")
            break
          if edit_flag == 1:
            change_in = input(f'Данные в справочнике были изменены, сохранить изменения в файл? 1- Да, 0- Нет\n:>>>')
            try:
              change_in = int(change_in)
              if change_in == 0:
                break
              if change_in == 1:
                print("Работа со спровочником завершена. Выход из программы")
                with open('phones.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                break
              elif change_in<0 or change_in>1:
                print("Введено некорректное значение меню.")
            except ValueError:
                print("Введено некорректное значение меню.")
      elif menu_num == 1:
          print_dict(data)

      elif menu_num == 2:
          while True:
           search_in = input("Выберите вариант поиска:\n 1- По имени\n 2- По номеру\n 3- По комментарию\n 0- Выход из меню поиска:\n>>> ")
           try:
             search_in = int(search_in)
             if search_in == 0:
                 print("Работа с поиском завершена. Выход в главное меню")
                 break

             if search_in == 1:
                 search_name = input(f'Введите имя:\n>>>')
                 data_search = search_func('name', search_name)
                 print_dict(data_search)

             if search_in == 2:

                 search_phone = input(f'Введите номер телефона(должен содержать только цифры):\n>>> ')
                 if not search_phone.isdigit():
                    print('Неверно введен номер телефона')
                    search_phone = input(f'Введите номер телефона(должен содержать только цифры):\n>>>')

                 data_search = search_func('phone', search_phone)
                 print_dict(data_search)

             if search_in == 3:
                 search_desc = input(f'Введите комментарий:\n>>>')
                 data_search = search_func('desc', search_desc)
                 print_dict(data_search)
             elif search_in > 3 or search_in < 0:
              print("Введено некорректное значение меню.")
           except ValueError:
             print("Введено некорректное значение меню.")
      elif menu_num == 3:
         while True:
          update_in = input("Выберите пункт меню изменения контакта:\n 1- По имени\n 2- По номеру\n 0- Выход из меню правки:\n>>> ")
          try:
              update_in = int(update_in)
              if update_in == 0:
                  print("Работа с правкой завершена. Выход из меню")
                  break
              if update_in == 1:
                  while True:
                   update_name_in = input("Выберите пункт меню изменения данных:\n 1- Исправить номер телефона\n 2- Исправить комментарий\n 0- Выход из меню правки:\n>>> ")
                   try:
                     update_name_in = int(update_name_in)
                     if update_name_in == 0:
                         print("Работа с правкой завершена. Выход из меню")
                         break
                     update_name = input(f'Введите имя:\n>>>')
                     data_search = search_func('name', update_name)
                     if not bool(data_search):
                         print('Данные отсутсвуют\n')
                         break
                     #print(data_search)
                     data_list = list(data_search)
                     update_key = data_list[0]
                     if update_name_in == 1:
                        update_data = input(f'Введите новое значение телефона:\n>>>')
                        update_type='phone'
                        update_val=update_data
                        update_func(update_key, update_type, update_val)
                        data_search = search_func('name', update_name)
                        print(f'Результат изменения:\n')
                        edit_flag = 1
                        print_dict(data_search)
                     if update_name_in == 2:
                        update_data = input(f'Введите новое значение комментария:\n>>>')
                        update_type='desc'
                        update_val=update_data
                        update_func(update_key, update_type, update_val)
                        data_search = search_func('name', update_name)
                        print(f'Результат изменения:\n')
                        print_dict(data_search)
                        edit_flag = 1
                     elif menu_num > 3 or menu_num < 0:
                        print("Введено некорректное значение меню.")

                   except ValueError:
                     print("Введено некорректное значение меню.")

              if update_in == 2:
                  while True:
                      update_phone_in = input("Выберите пункт меню изменения данных:\n 1- Исправить имя\n 2- Исправить комментарий\n 0- Выход из меню изменения:\n>>> ")
                      try:
                          update_phone_in = int(update_phone_in)
                          if update_phone_in == 0:
                              print("Работа с правкой завершена. Выход из меню")
                              break
                          update_phone_in = input(f'Введите номер телефона(должен содержать только цифры):\n>>>')
                          if not update_phone_in.isdigit():
                              print('Неверно введен номер телефона')
                              update_phone_in = input(f'Введите номер телефона(должен содержать только цифры):\n>>>')

                          data_search = search_func('phone', update_phone_in)
                          if not bool(data_search):
                              print('Данные отсутсвуют\n')
                              break
                          print(data_search)
                          data_list = list(data_search)
                          update_key = data_list[0]
                          if update_name_in == 1:
                              update_data = input(f'Введите новое значение имени:\n>>>')
                              update_type = 'name'
                              update_val = update_data
                              update_func(update_key, update_type, update_val)
                              data_search = search_func('phone', update_phone_in)
                              print(f'Результат изменения:\n')
                              print_dict(data_search)
                              edit_flag = 1
                          if update_name_in == 2:
                              update_data = input(f'Введите новое значение комментария:\n>>>')
                              update_type = 'desc'
                              update_val = update_data
                              update_func(update_key, update_type, update_val)
                              data_search = search_func('phone', update_phone_in)
                              print(f'Результат изменения:\n')
                              print_dict(data_search)
                              edit_flag = 1
                          elif menu_num > 3 or menu_num < 0:
                              print("Введено некорректное значение меню.")

                      except ValueError:
                          print("Введено некорректное значение меню.")

              elif menu_num > 3 or menu_num < 0:
                  print("Введено некорректное значение меню.")

          except ValueError:
              print("Введено некорректное значение меню.")

      elif menu_num == 4:
          while True:
              delete_in = input("Выберите пункт меню удаления контакта:\n 1- По имени\n 2- По номеру\n 0- Выход из меню удаления:\n>>> ")
              try:
                  delete_in = int(delete_in)
                  if delete_in == 0:
                      print("Работа с удалением завершена. Выход из меню")
                      break
                  if delete_in == 1:
                      delete_name = input(f'Введите имя:\n>>>')
                      data_delete= search_func('name', delete_name)
                      if not bool(data_delete):
                          print('Данные отсутсвуют\n')
                          break

                      print(data_delete)
                      data_list = list(data_delete)
                      update_key = data_list[0]
                      data.pop(update_key)
                      edit_flag = 1
                  if delete_in == 2:
                      delete_name = input(f'Введите номер телефона:\n>>>')
                      data_delete= search_func('phone', delete_name)
                      if not bool(data_delete):
                          print('Данные отсутсвуют\n')
                          break

                      print(data_delete)
                      data_list = list(data_delete)
                      update_key = data_list[0]
                      data.pop(update_key)
                      edit_flag = 1
                  elif delete_in > 2 or delete_in < 0:
                      print("Введено некорректное значение меню.")

              except ValueError:
                  print("Введено некорректное значение меню.")

      elif menu_num == 5:
          #while True:
            last_key = list(data)[-1]
            print(last_key)
            new_name = input(f'Введите имя:\n>>>')
            new_phone = input(f'Введите номер телефона(должен содержать только цифры):\n>>>')
            if not new_phone.isdigit():
              print('Неверно введен номер телефона')
              new_phone = input(f'Введите номер телефона(должен содержать только цифры):\n>>>')
            new_desc = input(f'Введите комментарий:\n>>>')
            new_key = int(last_key) + 1
            new_contact= { str(new_key): {'name': new_name, 'phone': new_phone, 'desc': new_desc}}
            data.update(new_contact)
            edit_flag = 1

      elif menu_num > 5 or menu_num<0:
        print("Введено некорректное значение меню.")
    except ValueError:
      print("Введено некорректное значение меню.")
