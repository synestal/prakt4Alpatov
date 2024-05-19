"""Телефонные номера"""
import re


def normalize_phone_numbers(text):
    """Нормализатор"""
    # Паттерн для поиска телефонных номеров
    phone_pattern = re.compile(r'\+?\d{1,3}\s?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}')

    def repl(match):
        """Proceed"""
        # Извлекаем номер телефона из найденного совпадения
        phone_number = match.group(0)

        # Извлекаем код страны из номера (первая цифра)
        country_code = '+' + phone_number[1]

        # Удаляем все символы, кроме цифр из номера
        digits = re.sub(r'\D', '', phone_number)

        # Форматируем номер телефона
        formatted_number = (f'{country_code} '
                            f'({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:]}')
        return formatted_number

    # Замена всех найденных номеров в тексте
    normalized_texthere = re.sub(phone_pattern, repl, text)
    return normalized_texthere


# Пример использования
INPUT_TEXT = """
Раз два три:
+14567890123, аываы в+4567890123456, ываыв а+78901234567ываыв аыва ыва ыва.
"""

normalized_text = normalize_phone_numbers(INPUT_TEXT)
print("Нормализованный текст:")
print(normalized_text)
