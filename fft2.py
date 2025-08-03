Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.array([[5,3,0,2],[1,7,8,3],[4,2,2,2],[8,5,2,1]])
>>> a
array([[5, 3, 0, 2],
       [1, 7, 8, 3],
       [4, 2, 2, 2],
       [8, 5, 2, 1]])
>>> np.fft.fft2(a)
array([[ 55. +0.j,   6. -9.j,   5. +0.j,   6. +9.j],
       [  0. -3.j,   3.+12.j,  -2. +5.j,   3.+14.j],
       [-15. +0.j,   8. +7.j,  -1. +0.j,   8. -7.j],
       [  0. +3.j,   3.-14.j,  -2. -5.j,   3.-12.j]])
>>> 