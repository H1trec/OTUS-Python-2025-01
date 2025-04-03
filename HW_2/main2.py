from controller import PhonebookController

def main():
    filename = 'phones.json'
    controller = PhonebookController(filename)
    controller.run()

if __name__ == '__main__':
    main()