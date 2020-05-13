
def decorator(function):
    def wrapper(numbers):
        print("Привет! я функция которая показывает количество четных чисел!")
        a = function(numbers)
        if a > 5:
            print("много:", a)
        elif a == 0:
            print("нету")
        else:
            print("ошибка данных")
        print("Хорошего дня!")
    return wrapper

@decorator
def list(numbers):
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += 1
    return sum
list([2,4,2,4,2,4,2])
