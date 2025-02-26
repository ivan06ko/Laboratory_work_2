import os  # Додаємо бібліотеку для роботи з файлами
from collections import Counter

def calculate_distance(left_list, right_list):
    """
    Обчислює загальну відстань між числами у двох списках після сортування.
    """
    if not left_list or not right_list:  # Перевірка, чи списки не порожні
        return 0
    
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    return sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))


def calculate_similarity_score(left_list, right_list):
    """
    Обчислює коефіцієнт схожості між двома списками.
    """
    if not left_list or not right_list:
        return 0
    
    right_count = Counter(right_list)
    return sum(num * right_count[num] for num in left_list)


def read_input_file(file_path):
    """
    Зчитує числа з файлу та повертає два списки чисел.
    """
    if not os.path.exists(file_path):  # Перевіряємо, чи існує файл
        print(f"Помилка: Файл {file_path} не знайдено!")
        return [], []

    left_list, right_list = [], []
    
    with open(file_path, 'r') as file:
        for line in file:
            try:
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
            except ValueError:
                print(f"Помилка у рядку: {line.strip()} (пропущено)")

    return left_list, right_list


if __name__ == "__main__":
    file_path = "input.txt"  # Вказуємо ім'я файлу без зайвих підпапок

    left_list, right_list = read_input_file(file_path)

    if left_list and right_list:  # Перевіряємо, чи є дані для обчислень
        total_distance = calculate_distance(left_list, right_list)
        print(f"Загальна сума відстаней: {total_distance}")

        similarity_score = calculate_similarity_score(left_list, right_list)
        print(f"Коефіцієнт схожості: {similarity_score}")
    else:
        print("Файл порожній або містить некоректні дані.") #Покищо у розробці, мучаю і вчусь дтп 
