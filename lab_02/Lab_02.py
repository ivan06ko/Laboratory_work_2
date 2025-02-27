def is_stable(report):
    """
    Перевіряє, чи є список чисел "стабільним".
    
    Умови:
    1. Числа повинні бути або в порядку зростання, або в порядку спадання.
    2. Різниця між сусідніми значеннями має бути в межах від 1 до 3 включно.

    :param report: список чисел (рядок із файлу)
    :return: True, якщо список стабільний, False - якщо ні
    """
    ascending = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    descending = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    if not (ascending or descending):  # Якщо числа не впорядковані, список нестабільний
        return False
    
    return all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))


def can_be_made_stable(report):
    """
    Додаткове завдання: перевіряє, чи можна зробити список стабільним, видаливши один елемент.

    :param report: список чисел
    :return: True, якщо можна зробити стабільним шляхом видалення одного елемента, False - якщо ні
    """
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Видаляємо один елемент
        if is_stable(modified_report):
            return True
    return False


def count_stable_reports(file_path):
    """
    Зчитує дані з файлу та підраховує кількість стабільних записів.

    :param file_path: шлях до вхідного файлу
    :return: (кількість стабільних звітів, кількість виправлених звітів)
    """
    stable_count = 0
    fixed_stable_count = 0

    try:
        with open(file_path, 'r') as file:  # Відкриваємо файл для читання
            for line in file:
                numbers = list(map(int, line.split()))  # Конвертуємо рядок у список чисел
                if is_stable(numbers):
                    stable_count += 1
                elif can_be_made_stable(numbers):
                    fixed_stable_count += 1
        
        return stable_count, stable_count + fixed_stable_count
    
    except FileNotFoundError:
        print(f"Не вдалося знайти файл: {file_path}")
        return None, None


# --- Основна програма ---
input_file = "./WEB-Back-end-/Lab_2/input.txt"  # Шлях до файлу

# Виконуємо підрахунок
stable_reports, total_fixed_reports = count_stable_reports(input_file)

# Вивід результатів
if stable_reports is not None:
    print(f"Кількість стабільних звітів: {stable_reports}")
    print(f"Кількість звітів, що стали стабільними після корекції: {total_fixed_reports}")
#я просто зара експерементую і намагаюсь щось зробити, ще підуть  роботи і роботи
#не забути купити собачий корм курячий 450грам
