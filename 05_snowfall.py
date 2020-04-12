# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

sd.resolution = (1200, 600)

N = 2

snow_list = list() # структура (координата х, длина луча)
snow_list_last = list() # для запоминания предыдущей точки
for _ in range(0,N):
    snow_list.append((randint(0,1200), randint(10, 50)))

print(snow_list)
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

y = 500

while True:
    sd.start_drawing()
    for ind,snow in enumerate(snow_list):
        x = snow[0]
        delta = randint(-3,3)
        length = snow[1]
        snow_list[ind] = (x+delta, length)

        point = sd.get_point(x,y)

        if y > 50:
             try:
                 sd.snowflake(center=snow_list_last[ind], length=length, color=sd.background_color)
             except:
                 pass
             point = sd.get_point(x, y)
             sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
             last_point = point

             try:
                snow_list_last[ind] = point
             except:
                 snow_list_last.append(point)

        y -= 1

    if y < 30:
        y=500
        snow_list_last.clear()

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


