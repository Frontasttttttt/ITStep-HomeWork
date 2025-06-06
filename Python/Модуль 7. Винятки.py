#    //   / /
#   //___         __        ___         __     __  ___     ___        ___     __  ___  __  ___
#  / ___        //  ) )   //   ) )   //   ) )   / /      //   ) )   ((   ) )   / /      / /
# //           //        //   / /   //   / /   / /      //   / /     \ \      / /      / /
#//           //        ((___/ /   //   / /   / /      ((___( (   //   ) )   / /      / /



#Ex1
try:
    имя = input("Введите своё имя >>> ")
    возраст = int(input("Введите свой возраст >>> "))
    if возраст < 0 or возраст > 130:
        raise ValueError("Возраст должен быть в пределах от 0 до 130.")
    print(f"Привет, {имя}! Твой возраст — {возраст}.")
except ValueError as e:
    print(f"Ошибка >>> {e}")



#Ex2 >>> v.1
def приветствие(имя, возраст):
    if возраст < 0 or возраст > 130:
        raise ValueError("Возраст должен быть в пределах от 0 до 130.")
    return f"Привет, {имя}! Твой возраст — {возраст}."

try:
    имя = input("Введите своё имя >>> ")
    возраст = int(input("Введите свой возраст >>> "))
    print(приветствие(имя, возраст))
except ValueError as e:
    print(f"Ошибка >>> {e}")



#Ex2 >>> v.2
def приветствие_с_обработкой(имя, возраст):
    try:
        if возраст < 0 or возраст > 130:
            raise ValueError("Возраст должен быть в пределах от 0 до 130.")
        return f"Привет, {имя}! Твой возраст — {возраст}."
    except ValueError as e:
        return f"Ошибка >>> {e}"

имя = input("Введите своё имя >>> ")
возраст = int(input("Введите свой возраст >>> "))
print(приветствие_с_обработкой(имя, возраст))



#Ex3
try:
    числа = []
    while True:
        число = int(input("Введите положительное число (или 0 для завершения) >>> "))
        if число == 0:
            break
        if число < 0:
            raise ValueError("Число не может быть отрицательным.")
        числа.append(число)
    print(f"Сумма чисел >>> {sum(числа)}")
except ValueError as e:
    print(f"Ошибка >>> {e}")



#Ex4 >>> v.1
def вычислить_сумму(числа):
    for число in числа:
        if число < 0:
            raise ValueError("Число не может быть отрицательным.")
    return sum(числа)

try:
    числа = []
    while True:
        число = int(input("Введите положительное число (или 0 для завершения) >>> "))
        if число == 0:
            break
        числа.append(число)
    print(f"Сумма чисел >>> {вычислить_сумму(числа)}")
except ValueError as e:
    print(f"Ошибка >>> {e}")



#Ex4 >>> v.2
def вычислить_сумму_с_обработкой(числа):
    try:
        for число in числа:
            if число < 0:
                raise ValueError("Число не может быть отрицательным.")
        return sum(числа)
    except ValueError as e:
        return f"Ошибка >>> {e}"

числа = []
while True:
    число = int(input("Введите положительное число (или 0 для завершения) >>> "))
    if число == 0:
        break
    числа.append(число)
результат = вычислить_сумму_с_обработкой(числа)
print(f"Результат >>> {результат}")