"""Brown Islands
Developer: Turchinovich Maria
"""

from turtle import penup, pendown, goto, mainloop, speed
from random import random
from math import sqrt

def brown (x0, y0, x1, y1, disp, p, n=8, m=500):
     ''' Рекурсивная функция построения Броуновского моста.
     Параметры:
     x0, y0, x1, y1 - координаты двух точек
     disp -дисперсия
     p - плавность
     n - глубина рекурсии
     m - масштаб

     xm, ym - координаты середины
     delta - смещение
     '''
     speed(10)
     if n == 0:
          penup()
          goto(x0 * m - m / 2, y0 * m - m / 2)
          pendown()
          goto(x1 * m - m / 2, y1 * m - m / 2)
          return
     xm = (x0 + x1) / 2.0
     ym = (y0 + y1) / 2.0
     delta_x = random() * sqrt(disp)
     delta_y = random() * sqrt(disp)
     brown(x0, y0, xm + delta_x, ym + delta_y, disp / p, p, n - 1)
     brown(xm + delta_x, ym + delta_y, x1, y1, disp / p, p, n -1 )

def main():
     h = float(input())
     speed(10)
     a = 2.0 ** (2.0 * h)
     brown(0.0, 0.0, 0.0, 0.0, 0.5, a)
     mainloop()


if __name__ == '__main__':
    main()