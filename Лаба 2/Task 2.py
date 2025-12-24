def describe_person(name, age=30):
    return f"Имя: {name} Возраст: {age}"
u_n = input("Введите имя: ")
u_a = input("Введите возраст: ")
if u_a:
    print(describe_person(u_n, u_a))
else:
    print(describe_person(u_n))