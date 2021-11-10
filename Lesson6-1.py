import random

my_list1 = [random.randint(1, 10) for _ in range(5)]
my_list2 = [random.randint(1, 10) for _ in range(5)]
my_list3 = []
for num in my_list1 + my_list2:
    if num not in my_list3:
        my_list3.append(num)
print("Кол-во уникальных чисел:", len(my_list3))
