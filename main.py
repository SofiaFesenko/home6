from collections import UserDict


class AddressBook(UserDict):
    def has_in_keys(self, key):
        return key in self.data.keys()


class Field():
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @staticmethod
    def add():
        name = input('input name')
        address_dict[phone] = name
        print(address_dict)

    @staticmethod
    def update():
        new_name = input('input new name')
        address_dict[phone] = new_name
        print(address_dict)

    @staticmethod
    def destroy():
        del address_dict[phone]
        print(address_dict)


class Record(Field):
    @staticmethod
    def add():
        name = input('input name')
        address_dict[phone] = name
        with open('phonebook.txt', mode='w') as f:
            f.write(f'{address_dict} \n')
        print(address_dict)

    @staticmethod
    def update():
        new_name = input('input new name')
        address_dict[phone] = new_name
        with open('phonebook.txt', mode='w') as f:
            f.write(f'{address_dict} \n')
        print(address_dict)

    @staticmethod
    def destroy():
        del address_dict[phone]
        with open('phonebook.txt', mode='w') as f:
            f.write(f'{address_dict} \n')
        print(address_dict)


address_dict = AddressBook()
while True:
    search = input('do you want to search user(by name!!)? (y if yes, n if no)')
    if search == 'y':
        search_name = input('input a name')
        with open('phonebook.txt', 'r') as p:
            lines = p.readlines()
            for line in lines:
                if line.find(search_name) != -1:
                    print(line)
    else:
        phone = input('input phone number or break(if you want to exit)')
        if phone != 'break':
            with open("phonebook.txt", "r") as p:
                phonebook = p.read()
                if phone not in phonebook:
                    print('you don`t have this number')
                    Record.add()
                else:
                    ans = input('you already have this number. do you want to update it or delete? (u/d)')
                    if ans == 'u':
                        Record.update()
                    else:
                        Record.destroy()
        else:
            break

