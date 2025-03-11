import re

def parse_game(line):
    """Розбирає рядок з інформацією про гру."""
    game_id, sets = line.split(": ")
    game_id = int(game_id.split()[1])
    
    cube_sets = []
    for subset in sets.split("; "):
        cube_dict = {"red": 0, "green": 0, "blue": 0}
        for match in re.findall(r"(\d+) (red|green|blue)", subset):
            count, color = int(match[0]), match[1]
            cube_dict[color] = count
        cube_sets.append(cube_dict)
    
    return game_id, cube_sets

def is_game_possible(cube_sets, bag_limits):
    """Перевіряє, чи можлива гра з даними обмеженнями кубиків."""
    for cube_set in cube_sets:
        if any(cube_set[color] > bag_limits[color] for color in bag_limits):
            return False
    return True

def find_minimum_cubes(cube_sets):
    """Знаходить мінімальну кількість кубиків для гри."""
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for cube_set in cube_sets:
        for color in min_cubes:
            min_cubes[color] = max(min_cubes[color], cube_set[color])
    return min_cubes

def calculate_power(cube_counts):
    """Обчислює "потужність" набору кубиків як добуток їхньої кількості."""
    return cube_counts["red"] * cube_counts["green"] * cube_counts["blue"]

def main(file_path):
    """Основна функція для читання вхідного файлу та обробки ігор."""
    bag_limits = {"Червоний": 12, "Зелений": 13, "Чиній": 14}
    possible_games_sum = 0
    total_power_sum = 0
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                game_id, cube_sets = parse_game(line.strip())
                
                # Перевіряємо, чи можлива гра
                if is_game_possible(cube_sets, bag_limits):
                    possible_games_sum += game_id
                
                # Обчислюємо мінімальні необхідні кубики
                min_cubes = find_minimum_cubes(cube_sets)
                total_power_sum += calculate_power(min_cubes)
        
        print(f"Сума ID можливих ігор: {possible_games_sum}")
        print(f"Сума потужностей мінімальних наборів: {total_power_sum}")
    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")

# --- Виконання програми ---
file_path = "C:\\Users\\777\\Desktop\\Laboratory_work_2\\Laboratory_work_2\\lab_05\\input_5.txt"  # Шлях до вхідного файлу
main(file_path)
#??? версія коду. все стабільно