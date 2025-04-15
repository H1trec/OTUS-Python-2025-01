import unittest
from model import PhoneBook, Contact,FileReader,FileWriter
from ddt import ddt, data, unpack

@ddt
class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.phone_book = PhoneBook("test_phonebook.json")
        self.phone_book.contacts = {}
        self.phone_book.save_contacts()

    def tearDown(self):
        self.phone_book.contacts = {}
        self.phone_book.save_contacts()

    @data(("Test", "1111", "test", "Test"), ("Test2", "21111", "test2", "Test2"))
    @unpack
    def test_add_contact_valid(self, test_name, test_phone, test_desc, expected):

        self.phone_book.add_contact(test_name,test_phone,test_desc)
        search_results = self.phone_book.search_contact("name",test_name)
        results = list(self.phone_book.search_contact('phone', test_phone))
        search_id = results[0]
        if results:
            test_result = search_results[search_id]['name']
            self.assertEqual(test_result, expected)
        else:
            self.fail(f"Контакт с именем {test_name} не найден")

    @data(("Test", "11R11", "test"), ("Test2", "21R111", "test2"))
    @unpack
    def test_add_contact_invalid_phone(self, test_name,test_phone, test_desc ):
        with self.assertRaises(ValueError):
             self.phone_book.add_contact(test_name,test_phone,test_desc)
             self.phone_book.add_contact(test_name,test_phone,test_desc)
             self.assertEqual(str(context.exception), "Неверно введен номер телефона(должен содержать только цифры).")


    @data(("Test", "1111", "test"), ("Test2", "21111", "test2"))
    @unpack
    def test_search_contact_by_name(self, test_name,test_phone, test_desc ):
        self.phone_book.add_contact(test_name,test_phone,test_desc)
        search_results = self.phone_book.search_contact("name",test_name)
        results = list(self.phone_book.search_contact('phone', test_phone))
        search_id = results[0]
        self.assertEqual(search_results[search_id]['name'], test_name)

    @data(("Test", "1111", "test"), ("Test2", "21111", "test2"))
    @unpack
    def test_search_contact_by_phone(self, test_name,test_phone, test_desc):
        self.phone_book.add_contact(test_name,test_phone,test_desc)
        search_result = self.phone_book.search_contact('phone', test_phone)
        results = list(self.phone_book.search_contact('phone', test_phone))
        search_id = results[0]
        self.assertEqual(search_result[search_id]['name'], test_name)


    @data(("Test", "1111", "test","NoName"), ("Test2", "21111", "test2","NoName"))
    @unpack
    def test_search_contact_nonexistent(self, test_name,test_phone, test_desc,test_serch):
        with self.assertRaises(ValueError):
          self.phone_book.search_contact('name',test_serch)
          self.assertEqual(str(context.exception), "Контакт не найден.")



    @data(("Test", "1111", "test"), ("Test2", "21111", "test2"))
    @unpack
    def test_update_contact_valid(self, test_name,test_phone, test_desc):
        old_name = 'old_test'
        old_phone = '000000'
        old_desc = 'old_desc'
        self.phone_book.add_contact(old_name,old_phone,old_desc)
        search_result = self.phone_book.search_contact('phone', old_phone)
        results = list(self.phone_book.search_contact('phone', old_phone))
        search_id = results[0]
        self.phone_book.update_contact(search_id, test_name,test_phone, test_desc)
        results = self.phone_book.search_contact('phone',test_phone)
        self.assertEqual(search_result [search_id]['name'], test_name)

    def test_update_contact_nonexistent(self):
        with self.assertRaises(ValueError):
            results = list(self.phone_book.search_contact('phone', "21111"))
            search_id = results[0]
            self.phone_book.update_contact(search_id, phone="55555")



    @data(("Test", "1111", "test"), ("Test2", "21111", "test2"))
    @unpack
    def test_delete_contact_valid(self,test_name,test_phone, test_desc):
        with self.assertRaises(ValueError):
             self.phone_book.add_contact(test_name,test_phone, test_desc)
             search_result = self.phone_book.search_contact('phone', test_phone)
             results = list(self.phone_book.search_contact('phone', test_phone))
             search_id = results[0]
             self.phone_book.delete_contact(search_id)
             self.phone_book.search_contact('phone', test_phone)
             self.assertEqual(str(context.exception), "Контакт не найден.")


    @data(("Test", "1111", "test"), ("Test2", "21111", "test2"))
    @unpack
    def test_save_load_file(self,test_name,test_phone, test_desc):
        self.phone_book.add_contact(test_name,test_phone, test_desc)
        self.phone_book.save_contacts()
        new_phone_book = PhoneBook(filename="test_phonebook.json")
        search_result = self.phone_book.search_contact('phone', test_phone)
        results = list(self.phone_book.search_contact('phone', test_phone))
        search_id = results[0]
        self.assertEqual(search_result[search_id]['name'], test_name)

    def test_add_empty_contact(self):
        with self.assertRaises(ValueError):
            test_name = ''
            test_phone = ''
            test_desc = ''
            self.phone_book.add_contact(test_name,test_phone,test_desc)



if __name__ == "__main__":
    unittest.main()