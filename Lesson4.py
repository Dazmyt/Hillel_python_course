# Задание-1
a = "Это строка в которую {} новую строку"
input_string = input('Введите что-то')
a = a.format(input_string)
print(a)
# задание-2 почему лишний принт?
print(a.replace(input_string, "замена в строке"))
a = a.replace(input_string, "замена в строке")
# Длина строки
print(len(a))
# Итого да/нет
if "строка" in a:
    print("ДА")
else:
    print("Нет")

