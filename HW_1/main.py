import json
with open('phones.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
while True:
    main_in = input("Выберите пункт меню для работы со справочником:\n 1- Показать все контакты\n 2- Найти контакт\n 3- Изменить контакт\n 4-Удалить контакт\n 5-Создать контакт\n 0-Выход из меню и окончание работы\n>>> ")
    try:
      menu_num = int(main_in)
      if menu_num == 0:
         print("Работа со спровочником завершена. Выход из программы")
         break
      elif menu_num == 1:

          for idx, name in data.items():
              print(f'Контакт №{idx}')
              for key, value in name.items():
                  print(f'\t{key:<8} {value}')
              print()

      elif menu_num == 2:
          def search_func(search_key, search_val):

              #flag = True
              search_dict = dict(filter(lambda item: item['name'] == search_val, data.items()))
              #for search_names in data:
                 # if data[search_names]['name'] == search_val:
                      # print(f'Найдены контакты:\n')
                      # print(f'Имя:', data[search_names]['name'])
                      # print(f'Телефон:', data[search_names]['phone'])
                      # print(f'Примечание:', data[search_names]['desc'])
                      # print()
                      #flag = False
              #if flag:
                  # print('Контакт не найден')
              return search_dict

          while True:
           search_in = input("Выберите вариант поиска:\n 1- По имени\n 2- По номеру\n 3- По комментарию\n 4- Поиск по всему\n 0-Выход из меню поиска\n>>> ")
           try:
             search_in = int(search_in)
             if menu_num == 0:
                 print("Работа с поиском завершена. Выход в главное меню")
                 break
             if search_in == 1:
                 search_name = input(f'Введите имя:\n')
                 data_search = search_func("name", search_name)
                 for idx, name in data_search.items():
                     print(f'Контакт №{idx}')
                     for key, value in name.items():
                         print(f'\t{key:<8} {value}')
                     print()
           #  if search_in == 2:
           #  if search_in == 3:
           #  if search_in == 4:
             elif menu_num > 4 or menu_num < 0:
              print("Введено некорректное значение меню.")
           except ValueError:
             print("Введено некорректное значение меню.")
 #   elif menu_num == 3:
 #   elif menu_num == 4:
 #   elif menu_num == 5:
      elif menu_num > 5 or menu_num<0:
        print("Введено некорректное значение меню.")
    except ValueError:
      print("Введено некорректное значение меню.")
