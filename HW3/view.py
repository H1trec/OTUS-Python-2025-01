def print_menu():
    print("\nТелефонный справочник")
    print("1. Вывод всех контактов")
    print("2. Поиск по имени")
    print("3. Поиск по телефону")
    print("4. Добавление контакта")
    print("5. Удаление контакта по имени")
    print("6. Удаление контакта по телефону")
    print("7. Обновление контакта по имени")
    print("8. Обновление контакта по телефону")
    print("9. Выход")

def get_choice():
    while True:
        try:
            choice = int(input("Введите номер действия: "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("Неверный выбор. Пожалуйста, выберите от 1 до 9.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

def get_query():
    return input("Введите имя или телефон для поиска/удаления/обновления: ")

def get_contact_details():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    desc = input("Введите описание: ")
    return name, phone, desc


def display_contacts(contacts):
    if not bool(contacts):
        print('Данные отсутсвуют\n')
    for idx, name in contacts.items():
        print(f'Контакт №{idx}')
        for key, value in name.items():
            print(f'\t{key:<8} {value}')
        print()

def display_error(message):
    print(f"Ошибка: {message}")

def confirm_update():
    return input("Вы уверены, что хотите обновить этот контакт? (да/нет): ").lower() == 'да'

def confirm_save():
    return input("Данные в справочнике были изменены. Сохранить изменения в файле? (да/нет): ").lower() == 'да'


def get_new_contact_details():
    name = input(f"Введите новое имя: ")
    phone = input(f"Введите новый телефон: ")
    desc = input(f"Введите новое описание: ")
    return name, phone, desc