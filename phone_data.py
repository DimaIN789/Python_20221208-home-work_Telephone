# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. (txt - csv например).

def phone_data(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15))
        print("-"*20)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(20))
    else:
        print("no data available")

        