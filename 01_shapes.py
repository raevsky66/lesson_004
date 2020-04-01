# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
def triangle(point, leng, angle):
    new_point = point
    print(new_point is point)
    for i in range(0, 3):
        vector = sd.get_vector(new_point, angle * i, length=leng)
        vector.draw()
        new_point = vector.end_point
    sd.line(start_point=new_point, end_point=point)

def square(point, leng, angle):
    new_point = point
    print(new_point is point)
    for i in range(0, 4):
        vector = sd.get_vector(new_point, angle * i, length=leng)
        vector.draw()
        new_point = vector.end_point
    sd.line(start_point=new_point, end_point=point)

def pentagon(point, leng, angle):
    new_point = point
    print(new_point is point)
    for i in range(0, 5):
        vector = sd.get_vector(new_point, angle * i, length=leng)
        vector.draw()
        new_point = vector.end_point
    sd.line(start_point=new_point, end_point=point)

def hexagon(point, leng, angle):
    new_point = point
    print(new_point is point)
    for i in range(0, 6):
        vector = sd.get_vector(new_point, angle * i, length=leng)
        vector.draw()
        new_point = vector.end_point
    sd.line(start_point=new_point, end_point=point)


triangle(point=sd.get_point(100, 100), leng=50, angle=120)
square(point=sd.get_point(200, 200), leng=50, angle=90)
pentagon(point=sd.get_point(300, 300), leng=50, angle=72)
hexagon(point=sd.get_point(400, 400), leng=50, angle=60)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
