# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

def draw_branches(point, angle, length):
    if length < 7:
        return
    rand_angle = 30+ int(30*randint(-40,40)/100)
    v1 = sd.get_vector(start_point=point, angle=angle + rand_angle, length=length,width=1)
    v1.draw()
    next_point = v1.end_point
    next_angle = v1.angle
    next_length = v1.length * (0.75+0.75*int(randint(-20,20)/100))
    draw_branches(point=next_point, angle=next_angle,length=next_length)
    v2 = sd.get_vector(start_point=point, angle=angle - rand_angle, length=length,width=1)
    v2.draw()
    next_point = v2.end_point
    next_angle = v2.angle
    next_length = v2.length * (0.75+0.75*int(randint(-20,20)/100))
    draw_branches(point=next_point, angle=next_angle,length=next_length)

sd.resolution = (1200, 600)
start_point = sd.get_point(600,100)
start_angle = 90
start_length = 100
draw_branches(point=start_point, angle=start_angle,length=start_length)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


