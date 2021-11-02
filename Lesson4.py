# Задание-1
a = "Это строка в которую {} новую строку"
input_string = input('Введите что-то')
b = a.format(input_string)
print(b)
# задание-2
str = b
print(str.replace(input_string, "замена в строке"))
c = str.replace(input_string, "замена в строке")
# Длина строки
print(len(c))
# Итого да/нет
if "строка" in c:
    print("ДА")
else:
    print("Нет")

