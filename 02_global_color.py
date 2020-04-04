# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def triangle(point, leng, angle,color):
    figure(point=point, leng=leng, angle=angle, number_of_points=3,color=color)

def square(point, leng, angle,color):
    figure(point=point, leng=leng, angle=angle, number_of_points=4,color=color)

def pentagon(point, leng, angle,color):
    figure(point=point, leng=leng, angle=angle, number_of_points=5,color=color)

def hexagon(point, leng, angle,color):
    figure(point=point,leng=leng,angle=angle,number_of_points=6,color=color)

def figure(point, leng, angle, number_of_points, color):
    new_point = point
    for i in range(0, number_of_points-1):
        vector = sd.get_vector(new_point, angle * i, length=leng)
        vector.draw(color=color)
        new_point = vector.end_point
    sd.line(start_point=new_point, end_point=point, color=color)


colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
colors_text = ('COLOR_RED', 'COLOR_ORANGE', 'COLOR_YELLOW', 'COLOR_GREEN', 'COLOR_CYAN', 'COLOR_BLUE', 'COLOR_PURPLE')
for index,val in enumerate(colors_text):
    print(index, ': ',val)
while True:
    try:
        color_index = input("выберите цвет: ")
        color = colors[int(color_index)]
        break
    except:
        print('Неправильный ввод')

sd.resolution = (1200, 600)

triangle(point=sd.get_point(100, 100), leng=50, angle=120,color=color)
square(point=sd.get_point(200, 200), leng=50, angle=90,color=color)
pentagon(point=sd.get_point(300, 300), leng=50, angle=72,color=color)
hexagon(point=sd.get_point(400, 400), leng=50, angle=60,color=color)

sd.pause()
