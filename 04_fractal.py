# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

def draw_branches(point, angle, point_1, angle_1, length):
    # start_point1 = point
    # angle1 = angle
    # length1 = length

    # start_point2 = point
    # angle2 = angle
    # length2 = length

    if length < 10:
       return

    v1 = sd.get_vector(start_point=point, angle=angle + 30, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=point_1, angle=angle - 30, length=length)
    v2.draw()


v1 = sd.get_vector(start_point=point, angle=angle + 30, length=length)
v1.draw()
v2 = sd.get_vector(start_point=point_1, angle=angle - 30, length=length)
v2.draw()

    new_point = v1.end_point
    new_point_1 = v2.end_point
    new_angle = angle+30
    new_angle_1 = angle-30
    new_length = length *.75
    # new_length = length*.75
    # new_angle = angle - 30
    draw_branches(point=new_point, angle=new_angle, point_1= new_point_1, angle_1=new_angle_1,length=new_length)
    #draw_branches(point=v2.end_point, angle=new_angle, length=new_length)

    # while length2 > 10:
    #     v2=sd.get_vector(start_point=start_point2,angle=angle2-30,length=length2)
    #     v2.draw()
    #     length2 *= .75
    #     angle2 -=30
    #     draw_branches(point=v2.end_point, angle=angle2, length=length2)
    # if length1 < 5 and length2 < 5:
    #     return

sd.resolution = (1200, 600)
start_point = sd.get_point(600,100)
start_angle = 90
start_length = 100
draw_branches(point=start_point, angle=start_angle, point_1= start_point, angle_1=start_angle,length=start_length)
# for _ in range(0, 25):
#     start_point = draw_branches(point=start_point,angle=start_angle,length=start_length)
#     start_angle +=30
#     start_length *=.75

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

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


