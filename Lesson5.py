#При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
#представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
#может пригодится функция reversed() - использовать при итерации for i in reversed(range(n))
userInput=int(input("Введите количество этажей:"))
row=""
count =1
spacing =0
star=0
u=0
while(count <=userInput):
    spacing =spacing +count
    while(spacing<userInput):
        row+=" "
        spacing +=1
    star=count +u
    while(star>0):
        row+="*"
        star-=1
    count +=1
    spacing=0
    u+=1
    print(row)
    row*=-1