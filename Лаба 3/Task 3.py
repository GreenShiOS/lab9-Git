def read_file(file_path, method="all"):
    try:
        if method == "all":
            with open(file_path, "r", encoding="utf-8") as f:
                print(f.read())
        elif method == "lines":
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    print(line, end="")
        else:
            print("неизвестный метод, используйте 'all' или 'lines'.")
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден. Убедитесь, что он существует.")
F_L = input("Введите файл: ")
M = input("Введите метод('all' или 'lines'): ")
if M == "":
    read_file(F_L)
else:
    read_file(F_L, M)