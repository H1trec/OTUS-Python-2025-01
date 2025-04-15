from model import PhoneBook, FileReader,FileWriter
from view import print_menu, get_choice, get_query, get_contact_details, display_contacts, display_error, confirm_update, confirm_save, get_new_contact_details

class PhonebookController:
    def __init__(self, filename):
        self.address_book = PhoneBook(filename)

    def run(self):
        edit_flag = 0
        while True:
            print_menu()
            choice = get_choice()
            if choice == 1:
                self.address_book.display_contacts(self.address_book.contacts)

            if choice == 2:
                search_name = get_query()
                try:
                    results = self.address_book.search_contact('name', search_name)
                    display_contacts(results)
                except Exception as e:
                    display_error(str(e))

            if choice == 3:
                search_phone = get_query()
                if self.address_book.is_valid_phone(search_phone):
                  try:
                    results = self.address_book.search_contact('phone', search_phone)
                    display_contacts(results)
                  except Exception as e:
                    display_error(str(e))
                else:
                    print("Неверно введен номер телефона(должен содержать только цифры).")

            elif choice == 4:
                name, phone, desc = get_contact_details()
                try:
                    self.address_book.add_contact(name, phone, desc)
                    print(f"Контакт успешно добавлен.")
                    edit_flag = 1
                except InvalidContactDataError as e:
                    display_error(str(e))

            elif choice == 5:
                delete_name = get_query()
                try:
                    removed_contacts = self.address_book.search_contact('name', delete_name)
                    if removed_contacts:
                        data_list = list(removed_contacts)
                        delete_id = data_list[0]
                        self.address_book.delete_contact(delete_id)
                        print(f"Найденные и удалённые контакты:")
                        display_contacts(removed_contacts)
                        edit_flag = 1
                    else:
                        print(f"Контакты не найдены.")
                except Exception as e:
                    display_error(str(e))

            elif choice == 6:
                delete_phone = get_query()
                if self.address_book.is_valid_phone(delete_phone):
                  try:
                    removed_contacts = self.address_book.search_contact('phone', delete_phone)
                    if removed_contacts:
                        data_list = list(removed_contacts)
                        delete_id = data_list[0]
                        self.address_book.delete_contact(delete_id)
                        print(f"Найденные и удалённые контакты:")
                        display_contacts(removed_contacts)
                        edit_flag = 1
                    else:
                        print(f"Контакты не найдены.")
                  except Exception as e:
                    display_error(str(e))
                else:
                    print("Неверно введен номер телефона(должен содержать только цифры).")

            elif choice == 7:
                update_name = get_query()
                try:
                    update_contacts = self.address_book.search_contact('name', update_name)
                    if update_contacts:
                        for contact in update_contacts:
                            print(f"Найденный контакт:")
                            display_contacts(update_contacts)
                            data_list = list(update_contacts)
                            update_id = data_list[0]
                            if confirm_update():
                                new_name, new_phone, new_desc = get_new_contact_details()
                                self.address_book.update_contact(update_id, new_name, new_phone, new_desc)
                                print(f"Контакт успешно обновлен.")
                                edit_flag = 1
                    else:
                        print(f"Контакты не найдены.")
                except Exception as e:
                    display_error(str(e))

            elif choice == 8:
                update_name = get_query()
                try:
                    update_contacts = self.address_book.search_contact('phone', update_name)
                    if update_contacts:
                        for contact in update_contacts:
                            print(f"Найденный контакт:")
                            display_contacts(update_contacts)
                            data_list = list(update_contacts)
                            update_id = data_list[0]
                            if confirm_update():
                                new_name, new_phone, new_desc = get_new_contact_details()
                                self.address_book.update_contact(update_id, new_name, new_phone, new_desc)
                                print(f"Контакт успешно обновлен.")
                                edit_flag = 1
                    else:
                        print(f"Контакты не найдены.")
                except Exception as e:
                    display_error(str(e))

            elif choice == 9:
                if edit_flag == 1:
                    if confirm_save():
                        self.address_book.save_contacts()
                        break
                    else:
                        print(f"Изменения не были сохранены")
                else:
                 break