import re  # Імпортуємо модуль для роботи з регулярними виразами

# Словник відповідностей між словами та цифрами
WORD_TO_DIGIT = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def find_numeric_values(line):
    """
    Визначає першу і останню цифру в рядку.

    :param line: текстовий рядок
    :return: двозначне число (перша + остання цифра)
    """
    digits = [char for char in line if char.isdigit()]  # Вилучаємо цифри
    
    if digits:  # Якщо є хоча б одна цифра
        return int(digits[0] + digits[-1])  # Об'єднуємо першу та останню цифру
    
    return 0  # Якщо цифр немає, повертаємо 0


def find_spelled_numbers(line):
    """
    EXTRA TASK: знаходить першу і останню цифру, враховуючи числові слова.

    :param line: текстовий рядок
    :return: двозначне число (перша + остання цифра)
    """
    # Регулярний вираз для пошуку цифр і чисел, записаних словами
    pattern = r"one|two|three|four|five|six|seven|eight|nine|\d"
    matches = re.findall(pattern, line)  # Знаходимо всі збіги

    if matches:  # Якщо знайшли хоча б одне число
        first = WORD_TO_DIGIT.get(matches[0], matches[0])  # Перетворюємо слово на цифру
        last = WORD_TO_DIGIT.get(matches[-1], matches[-1])
        return int(first + last)  # Формуємо двозначне число
    
    return 0  # Якщо не знайдено жодного числа, повертаємо 0


def compute_calibration_sum(file_path):
    """
    Читає файл і підраховує суму калібрувальних значень.

    :param file_path: шлях до вхідного файлу
    :return: (сума з основного завдання, сума з EXTRA TASK)
    """
    sum_standard = 0  # Загальна сума для основного завдання
    sum_extended = 0  # Загальна сума для додаткового завдання

    try:
        with open(file_path, 'r') as file:  # Відкриваємо файл
            for line in file:
                sum_standard += find_numeric_values(line)  # Додаємо число з основного завдання
                sum_extended += find_spelled_numbers(line)  # Додаємо число з EXTRA TASK

        return sum_standard, sum_extended  # Повертаємо обидві суми
    
    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")
        return None, None


# --- Основний код ---
input_file = "C:\Users\777\Desktop\Laboratory_work_2\Laboratory_work_2\lab_03\input.txt"  # Шлях до файлу

# Обчислюємо результати
sum_main, sum_extra = compute_calibration_sum(input_file)

# Вивід результатів
if sum_main is not None:
    print(f"Сума калібрувальних значень (основне завдання): {sum_main}")
    print(f"Сума калібрувальних значень (EXTRA TASK): {sum_extra}")
#тичасовий код покищо готовий і занотований, треба буде в ньому поміняти 