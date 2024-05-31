# 1
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

if a >= 0:
    a = a ** 2
else:
    a = a ** 4

if b >= 0:
    b = b ** 2
else:
    b = b ** 4

if c >= 0:
    c = c ** 2
else:
    c = c ** 4

print("Результати обчислень: ", a, b, c)

# 2
x1 = float(input("Введіть координату x1 для точки A: "))
y1 = float(input("Введіть координату y1 для точки A: "))
x2 = float(input("Введіть координату x2 для точки B: "))
y2 = float(input("Введіть координату y2 для точки B: "))

distance_A = (x1**2 + y1**2) ** 0.5
distance_B = (x2**2 + y2**2) ** 0.5

if distance_A < distance_B:
    print("Точка A ближче до початку координат.")
else:
    print("Точка B ближче до початку координат.")

# 3
angle1 = float(input("Введіть перший кут (в градусах): "))
angle2 = float(input("Введіть другий кут (в градусах): "))

angle3 = 180 - (angle1 + angle2)

if angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("Такий трикутник існує.")
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Трикутник є прямокутним.")
    else:
        print("Трикутник не є прямокутним.")
else:
    print("Такий трикутник не існує.")

# 4
x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))

if x < y:
    x = (x + y) / 2
    y = x * y * 2
else:
    y = (x + y) / 2
    x = x * y * 2

print("Змінені значення: x =", x, ", y =", y)

# 5
x = float(input("Введіть координату x точки A: "))
y = float(input("Введіть координату y точки A: "))

if x == 0 and y == 0:
    print("Точка знаходиться в початку координат.")
elif x == 0:
    print("Точка знаходиться на осі Y.")
elif y == 0:
    print("Точка знаходиться на осі X.")
elif x > 0 and y > 0:
    print("Точка знаходиться в першому координатному куті.")
elif x < 0 and y > 0:
    print("Точка знаходиться в другому координатному куті.")
elif x < 0 and y < 0:
    print("Точка знаходиться в третьому координатному куті.")
else:
    print("Точка знаходиться в четвертому координатному куті.")

# 6
a = int(input("Введіть перше ціле число: "))
b = int(input("Введіть друге ціле число: "))

if a != b:
    max_val = max(a, b)
    a = max_val
    b = max_val
else:
    a = 0
    b = 0

print("Змінені значення: a =", a, ", b =", b)

# 7
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

negative_count = 0
if a < 0:
    negative_count += 1
if b < 0:
    negative_count += 1
if c < 0:
    negative_count += 1

print("Кількість негативних чисел:", negative_count)

# 8
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

positive_count = 0
if a > 0:
    positive_count += 1
if b > 0:
    positive_count += 1
if c > 0:
    positive_count += 1

print("Кількість додатних чисел:", positive_count)

# 9
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

integer_count = 0
if a.is_integer():
    integer_count += 1
if b.is_integer():
    integer_count += 1
if c.is_integer():
    integer_count += 1

print("Кількість цілих чисел:", integer_count)

# 10
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))
k = float(input("Введіть число k: "))

if a % k == 0:
    print(f"Число {k} є дільником числа {a}")
if b % k == 0:
    print(f"Число {k} є дільником числа {b}")
if c % k == 0:
    print(f"Число {k} є дільником числа {c}")
