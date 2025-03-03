def is_stable(report):
    """
    :param report: список чисел (рядок із файлу)
    :return: True, якщо список стабільний, False - якщо ні
    """
    ascending = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    descending = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    if not (ascending or descending):  # Якщо числа не впорядковані то список нестабільний
        return False
    
    return all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))


def can_be_made_stable(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Видаляємо один елемент
        if is_stable(modified_report):
            return True
    return False


def count_stable_reports(file_path):
    
    #Зчитує дані з файлу та підраховує кількість стабільних записів.

    #:param file_path: шлях до вхідного файлу
    #:return: (кількість стабільних звітів, кількість виправлених звітів)
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

input_file = "C:\Users\777\Desktop\Laboratory_work_2\Laboratory_work_2\lab_02\input.txt"  # Шлях до файлу

# Виконуємо підрахунок
stable_reports, total_fixed_reports = count_stable_reports(input_file)

# Вивід результатів
if stable_reports is not None:
    print(f"Кількість стабільних звітів: {stable_reports}")
    print(f"Кількість звітів, що стали стабільними після корекції: {total_fixed_reports}")
#Поправив посилання на текстовий документ
#сьогодні треба в спортазал йти...
