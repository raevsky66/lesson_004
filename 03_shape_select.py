# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = (1200, 600)


def triangle(point, leng, angle):
    figure(point=point, leng=leng, angle=angle, number_of_points=3)

def square(point, leng, angle):
    figure(point=point, leng=leng, angle=angle, number_of_points=4)

def pentagon(point, leng, angle):
    figure(point=point, leng=leng, angle=angle, number_of_points=5)

def hexagon(point, leng, angle):
    figure(point=point,leng=leng,angle=angle,number_of_points=6)

def figure(point, leng, angle, number_of_points):
    new_point = point
    for i in range(0, number_of_points-1):
        vector = sd.get_vector(new_point, angle * i, length=leng)
        vector.draw()
        new_point = vector.end_point
    sd.line(start_point=new_point, end_point=point)

center_point = sd.get_point(sd.resolution[0]/2, sd.resolution[1]/2)

figure_all = {0:'треугольник',1:'квадрат',2:'пятиугольник',3:'шестиугольник'}
for index, val in figure_all.items():
    print(index,':', val)

figure_choose = ''
while True:
    try:
        figure_number = input("выберите фигуру: ")
        figure_choose = figure_all[int(figure_number)]
        break
    except:
        print('Неправильный ввод')

if figure_choose == 'треугольник':
    triangle(point=center_point, leng=50, angle=120)
elif figure_choose == 'квадрат':
    square(point=center_point, leng=50, angle=90)
elif figure_choose == 'пятиугольник':
    pentagon(point=center_point, leng=50, angle=72)
else:
    hexagon(point=center_point, leng=50, angle=60)

sd.pause()
