SHAPE_SCORES = {'X': 1, 'Y': 2, 'Z': 3}  # вибір 
OUTCOME_SCORES = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                  ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                  ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}  # результат

def calculate_total_score(file_path):
    total_score = 0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                opponent, you = line.strip().split()  #вибори гравців
                total_score += SHAPE_SCORES[you] + OUTCOME_SCORES[(opponent, you)]
    
        return total_score
    except FileNotFoundError:
        print(f" Файл не знайдено: {file_path}")
        return None

# --- Основна програма ---
file_path = "C:\\Users\\777\\Desktop\\Laboratory_work_2\\Laboratory_work_2\\lab_06\\input_6.txt"  # Вкажи свій шлях до файлу
final_score = calculate_total_score(file_path)

if final_score is not None:
    print(f"Загальний рахунок: {final_score}")
#незнаю. привіт чи щось таке