import json

class Contact:
    def __init__(self, name, phone, desc):
        self.name = name
        self.phone = phone
        self.desc = desc

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "desc": self.desc
        }

class FileReader:
    @staticmethod
    def read(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Файл справочника не найден.")
            return {}
        except json.JSONDecodeError:
            print("Ошибка разбора JSON файла")
            return {}

class FileWriter:
    @staticmethod
    def write(filename, data):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class PhoneBook(Contact):
    def __init__(self, filename="phones.json"):
        super().__init__("", "", "")
        self.filename = filename
        self.contacts = FileReader.read(self.filename)
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            print(f"Файл справочника не найден.")
            self.contacts = {}

    def save_contacts(self):
        FileWriter.write(self.filename, self.contacts)

    def search_contact(self, search_key, search_name):
            search_val = {k: v for k, v in self.contacts.items() if v.get(search_key).casefold() == search_name.casefold()}
            return search_val

    def update_contact(self, id, name=None, phone=None, desc=None):
        if id in self.contacts:
            is_not_empty_name=name.isalnum()
            is_not_empty_desc=desc.isalnum()
            if  is_not_empty_name:
                self.contacts[id]["name"] = name
            if phone is not None and self.is_valid_phone(phone):
                self.contacts[id]["phone"] = phone
            if is_not_empty_desc:
                self.contacts[id]["desc"] = desc

        else:
            print(f"Контакт для изменения не найден.")

    def delete_contact(self, id):
        if id in self.contacts:
            del self.contacts[id]

        else:
            print(f"Контакт для удаления не найден.")

    def add_contact(self, name, phone, desc):
        new_id = str(max(int(k) for k in self.contacts.keys()) + 1)
        if self.is_valid_phone(phone):
            self.contacts[new_id] = {
                "name": name,
                "phone": phone,
                "desc": desc
            }
        else:
            print("Неверно введен номер телефона(должен содержать только цифры).")

    def is_valid_phone(self, phone):
        return phone.isdigit()

    def display_contacts(self,contacts):
        if not bool(contacts):
           print('Данные отсутсвуют\n')
        for idx, name in contacts.items():
           print(f'Контакт №{idx}')
           for key, value in name.items():
              print(f'\t{key:<8} {value}')
           print()