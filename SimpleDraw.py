import simple_draw as sd
from math import cos, sin, pi
from time import sleep

angle = 0
length = 100
x = y = 300
print(sin(90/180*pi))
for i in range(40):
    point = sd.get_point(x, y)
    v = sd.get_vector(start_point=point, length=length, angle=angle)
    v.draw()
    sd.circle(center_position=point, radius=10*cos(angle))
    print(point, x, y)
    x += length*cos(angle/180*pi)
    y += length*sin(angle/180*pi)
    angle += 110
    sleep(0.1)

sd.pause()