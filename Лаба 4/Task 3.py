from my_package import add, multiply, word_count

a = int(input("Введите число: "))
b = int(input("Введите число: "))
w = input("Введите слова: ")

s = add(a, b)
m = multiply(a, b)
wo = word_count(w)

print(f"Сумма: {s}")
print(f"Произведение: {m}")
print(f"Количествое слов: {wo}")