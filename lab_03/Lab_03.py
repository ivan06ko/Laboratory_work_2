import re 

def find_numeric_values(line):
    digits = [char for char in line if char.isdigit()] 
    
    if digits:  
        return int(digits[0] + digits[-1])  
    
    return 0  

def compute_calibration_sum(file_path):
    sum_standard = 0  

    try:
        with open(file_path, 'r') as file:  
            for line in file:
                sum_standard += find_numeric_values(line)  
        
        return sum_standard  
    
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        return None

# Основна частина коду 
input_file = "C:\\Users\\777\\Desktop\\Laboratory_work_2\\Laboratory_work_2\\lab_03\\input.txt"  # Шлях до файлу

# Результат
sum_main = compute_calibration_sum(input_file)
if sum_main is not None:
    print(f"Сума калібрувальних значень: {sum_main}")
