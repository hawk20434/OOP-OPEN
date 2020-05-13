
def count_mark():
    summa = 0
    print("Введите баллы за предметы(если вы их не сдавали нажмите entr)")
    marks = []
    math = int(input("Математика: "))
    marks.append(math)
    russ = int(input("Русский язык: "))
    marks.append(russ)
    inf = int(input("Информатика: "))
    marks.append(inf)
    for i in marks:
        summa += i
    return summa

def function(summa):
    if summa > 250:
        print("ура вы поступили!")
    elif summa > 180 and summa < 250:
        print(" Платка!")
    elif summa < 180:
        print("увы...")
    else:
        print("ошибка!")

print("Выбере направление подготовкии:\n"
      "1. Бизнес-Информатика\n"
      "2. Информационная безопастность\n"
      "3. Менеджмент")
chose = int(input("Выбор: "))
if chose == 1:
    function(summa=count_mark())
elif chose == 2:
    function(summa=count_mark())
elif chose == 3:
    function(summa=count_mark())
else:
    print("ошибка!проверьте правильность данных! ")








