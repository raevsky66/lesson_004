# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()

# sd.snowflake(center=point_0, length=200, factor_a=0.5)

# реализовать падение одной снежинки
y = 500
x = 100

y2 = 450
x2 = 150

point = sd.get_point(x, y)
point2 = sd.get_point(x2, y2)

sd.start_drawing()

while True:
#    sd.clear_screen()
    if y > 50:
        sd.snowflake(center=point, length=50, color=sd.background_color)
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=50)
        y -= 1

    x = x + 1

    if y2 > 30:
        sd.snowflake(center=point2, length=30, color=sd.background_color)
        point2 = sd.get_point(x2, y2)
        sd.snowflake(center=point2, length=30)
        y2 -= 6

    x2 = x2 + 3

    if y2<30 and y<50:
        break

    sd.sleep(0.1)
    if sd.user_want_exit():
        break
    sd.finish_drawing()
# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
