def writing(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content + '\n')

def adding(file_path, content):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content + '\n')

action = input("Введите действие: ")

if action == "Записать" or action == "записать":
    content = input("Введите текст для записи в файл: ")
    file_path = input("Введите файл: ")
    writing(file_path, content)
elif action == "Добавить" or action == "добавить":
    content = input("Введите текст для добавления в файл: ")
    file_path = input("Введите файл: ")
    adding(file_path, content)
else:
    print("Вы ввели неправильное действие, попробуйте снова.")