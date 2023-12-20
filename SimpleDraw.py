import simple_draw as sd
from math import cos, sin, pi
from time import sleep
import time

# angle = 0
# length = 100
# x = y = 200
# print(sin(90/180*pi))
# for i in range(40):
#     point = sd.get_point(x, y)
#     v = sd.get_vector(start_point=point, length=length, angle=angle)
#     v.draw()
#     sd.circle(center_position=point, radius=10*cos(angle))
#     print(point, x, y)
#     x += length*cos(angle/180*pi)
#     y += length*sin(angle/180*pi)
#     angle += 110
#     sleep(0.1)
# #
# lenght = 200
# point = sd.get_point(300, 300)


# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v3.draw()

# def triangle(point, angle=0):
#     v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
#     v1.draw(color=(167, 15, 12))
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=3)
#     v2.draw(color=(167, 15, 12))
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=3)
#     v3.draw(color=(167, 15, 12))
#
#
# point_0 = sd.get_point(100, 300)
# for angle in range(0, 361, 10):
#     triangle(point=point_0, angle=angle)
#     time.sleep(0.1)

# def branch(point, angle, length):
#     point2 = sd.get_point(300, 5)
#     v1 = sd.get_vector(start_point=point2, angle=angle, length=length)
#     v1.draw()
#     return v1.end_point
#
#
# next_point = branch(point=0, angle=90, length=100)
# next_point = branch(point=next_point, angle=90-30, length=100*0.75)


sd.pause()
