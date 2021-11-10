
list = [261, 111, 551, 112, 312, 453, 153, 400]
variable = 0
for num in range(1, len(list) - 1):
    if list[num-1] < list[num] > list[num+1]:
        variable += 1
print("Количество чисел, которые старше своих соседей:", variable)
