import numpy as npy
import sympy as sym
import math as mat

e_one = mat.e ** -2
e_two = sym.Rational(1, mat.e ** 2)
same = e_one == e_two
if same:
    print('same')
