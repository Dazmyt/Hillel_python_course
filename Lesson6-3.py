import random

my_list = [random.randint(130, 200) for num in range(15)]
boy = int(input("Укажите рост мальчика: "))
my_list.sort(reverse=True)
for pos in range(len(my_list)):
    if my_list[pos] < boy:
        break
print(pos + 1, "место в строю")
