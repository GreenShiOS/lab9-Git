
def max_of_two(x, y):
    if x > y:
        return(x)
    if x < y:
        return(y)
    if x == y:
        print("Вы ввели 2 одинаковых числа")
print(max_of_two(int(input("Введите первое число: ")), \
                  int(input("введите второе число: "))))