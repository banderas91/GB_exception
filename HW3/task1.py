import re

def parse_input(user_input):
    data = user_input.split()
    if len(data) != 6:
        raise ValueError(f"Неверное количество данных: {len(data)}")
    surname, name, patronymic, birth_date, phone_number, gender = data
    if not re.match(r'\d{2}.\d{2}.\d{4}', birth_date):
        raise ValueError(f"Неверный формат даты рождения: {birth_date}")
    try:
        phone_number = int(phone_number)
    except ValueError:
        raise ValueError(f"Неверный формат номера телефона: {phone_number}")
    if gender not in ['f', 'm']:
        raise ValueError(f"Неверный формат пола: {gender}")
    return surname, name, patronymic, birth_date, phone_number, gender

def save_data(surname, name, patronymic, birth_date, phone_number, gender):
    try:
        with open(f"{surname}.txt", "a") as f:
            f.write(f"{surname} {name} {patronymic} {birth_date} {phone_number} {gender}\n")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

def main():
    user_input = input("Введите данные: ")
    try:
        surname, name, patronymic, birth_date, phone_number, gender = parse_input(user_input)
        save_data(surname, name, patronymic, birth_date, phone_number, gender)
        print("Данные успешно сохранены")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()