import re


def normalize_phone_numbers_in_file(file_path):
    # Открываем файл и считываем его содержимое
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Паттерн для поиска телефонных номеров
    phone_pattern = re.compile(r'\+?\d{1,3}\s?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}')

    def repl(match):
        # Извлекаем номер телефона из найденного совпадения
        phone_number = match.group(0)

        # Извлекаем код страны из номера (первая цифра)
        country_code = '+' + phone_number[1]

        # Удаляем все символы, кроме цифр из номера
        digits = re.sub(r'\D', '', phone_number)

        # Форматируем номер телефона
        formatted_number = '{} ({}) {}-{}-{}'.format(country_code, digits[1:4], digits[4:7], digits[7:9], digits[9:])
        return formatted_number

    # Замена всех найденных номеров в тексте
    normalized_text = re.sub(phone_pattern, repl, text)

    # Записываем измененный текст обратно в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(normalized_text)


# Пример использования
file_path = 'input.txt'  # Путь к вашему файлу с текстом
normalize_phone_numbers_in_file(file_path)
print("Телефонные номера в файле успешно нормализованы.")