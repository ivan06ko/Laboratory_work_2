def parse_terminal_output(file_path):
    """
    Аналізує вивід терміналу та створює структуру директорій.

    :param file_path: шлях до файлу
    :return: словник, що відображає файлову систему
    """
    fs_tree = {"/": {}}  # Ініціалізуємо кореневу директорію
    current_path = []  # Список для збереження поточного шляху

    try:
        with open(file_path, "r") as file:  # Використовуємо with для безпечного відкриття файлу
            for line in file:
                parts = line.strip().split()

                if parts[0] == "$":  # Обробка команд терміналу
                    if parts[1] == "cd":
                        if parts[2] == "/":  # Перехід до кореневої директорії
                            current_path = []
                        elif parts[2] == "..":  # Перехід на рівень вище
                            if current_path:
                                current_path.pop()
                        else:  # Перехід до вказаної директорії
                            current_path.append(parts[2])
                
                elif parts[0] == "dir":  # Виявлено директорію
                    dir_name = parts[1]
                    current_dir = get_nested_dir(fs_tree, current_path)
                    current_dir[dir_name] = {}
                
                else:  # Виявлено файл (формат: <розмір> <назва>)
                    file_size = int(parts[0])
                    file_name = parts[1]
                    current_dir = get_nested_dir(fs_tree, current_path)
                    current_dir[file_name] = file_size
        
        return fs_tree
    except FileNotFoundError:
        print(f"⚠️ Файл не знайдено: {file_path}")
        return None


def get_nested_dir(fs_tree, path):
    """
    Повертає вкладену директорію за вказаним шляхом.

    :param fs_tree: структура файлової системи
    :param path: список директорій, що визначає шлях
    :return: вкладений словник (поточна директорія)
    """
    current = fs_tree["/"]
    for directory in path:
        current = current[directory]
    return current


def calculate_directory_sizes(fs_tree, path="/"):
    """
    Рекурсивно обчислює розміри всіх директорій.

    :param fs_tree: структура файлової системи
    :param path: поточний шлях
    :return: словник {директорія: розмір}
    """
    sizes = {}
    
    def helper(node, full_path):
        total_size = 0
        for name, value in node.items():
            if isinstance(value, dict):  # Якщо це вкладена директорія
                dir_size = helper(value, f"{full_path}/{name}")
                sizes[f"{full_path}/{name}"] = dir_size
                total_size += dir_size
            else:  # Це файл
                total_size += value

        return total_size

    root_size = helper(fs_tree["/"], "/")
    sizes["/"] = root_size  # Додаємо кореневу директорію
    return sizes


# --- Головна частина програми ---
file_path = "C:\Users\777\Desktop\Laboratory_work_2\Laboratory_work_2\lab_04\input.txt"  # Шлях до файлу

# Розбираємо файлову систему
fs_tree = parse_terminal_output(file_path)

if fs_tree:
    # Обчислюємо розміри директорій
    dir_sizes = calculate_directory_sizes(fs_tree)

    # Вибираємо директорії з розміром ≤ 100000
    filtered_sizes = {k: v for k, v in dir_sizes.items() if v <= 100000}

    # Підраховуємо загальну суму
    total_size = sum(filtered_sizes.values())

    print(f"Сума розмірів директорій ≤ 100000: {total_size}")
#знову цей шматок коду. працюю над ним, а ще треба якось сімейні речі встигати робити... 