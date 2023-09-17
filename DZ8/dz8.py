menu = '''Главное меню
1. Открыть файл
2. Сохранить файл
3. Показать контакты
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход'''
phone_book = {}
path = 'phones.txt'


def save_file():
    contacts = []
    for contact in phone_book.values():
        contacts.append('; '.join(contact))
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(contacts))



def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        phone_book[i] = contact


def show_contact(pb):
    for k, v in pb.items():
        print(f'{k}. {v[0]}, {v[1]}, {v[2]}')

def new_contact():
    name = input('Введите фамилию и имя контакта : ')
    phone = input('Введите телефон контакта : ')
    comment = input('Введите описание контакта: ')
    phone_book[max(phone_book) + 1] = [name, phone, comment]


def change_contact():
    find_contact()
    id_ = int(input('Введите номер контакта, который хотите изменить: '))
    name = phone_book.get(id_)[0]
    new_name = input('Введите новые фамилию и имя контакта : ')
    if new_name == "":
        phone_book[id_][0] = name
    else:
        phone_book[id_][0] = new_name
    new_phone = input('Введите новый телефон контакта : ')
    phone = phone_book.get(id_)[1]
    if new_phone == "":
        phone_book[id_][1] = phone
    else:
        phone_book[id_][1] = new_phone
    new_comment = input('Введите новое описание контакта: ')
    comment = phone_book.get(id_)[2]
    if new_comment == "":
        phone_book[id_][2] = comment
    else:
        phone_book[id_][2] = new_comment


def delite_contact():
    find_contact()
    id_ = int(input('Введите номер контакта, который хотите удалить: '))
    phone_book.pop(id_)





def find_contact():
    result = {}
    search = input('Введите ключевое слово для поиска: ')
    for k, v in phone_book.items():
        for item in v:
            if search in item:
                result[k] = v
    show_contact(result)






while True:
    print(menu)
    choice = int(input('Выберите пункт меню: '))
    match choice:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contact(phone_book)
        case 4:
            new_contact()
        case 5:
            find_contact()
        case 6:
            change_contact()
        case 7:
            delite_contact()
        case 8:
            print('Выход из программы')
            break
        case _:
            print('Неверный пункт меню, попробуйте еще раз')