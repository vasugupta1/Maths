from sympy import *
from sympy.plotting import plot3d
import math

def plot():
    x, y = symbols('x y')
    f = 2*x + 3*y
    plot3d(f)

def another_way():
    i,n = symbols('i n')
    summation = Sum(2*i, (i, 1,n))
    up_to_5 = summation.subs(n ,5 )
    print(up_to_5.doit())

def logs():
    x = log(8,2)
    print(x)

def cal_total_compound(p: int, r:float, t:float, n:int):
    a = 1 + (r/n)
    print(p * a **(n*t))
    

def euler_compouding_rule(p: int, r: float, t: int):
    a = p * exp(r*t)
    print(a)

def limits():
    x = symbols('x')
    f = 1/x
    result = limit(f, x, oo)
    print(result)


def my_function(x):
    y = x**2
    return y

def calculate_slop(f, x, step_size):
    top = f(x + step_size) - f(x)
    bottom = (x+step_size) - x
    m = top / bottom
    return m

def better_way_for_derivates(val):
    return 2*val


def f(x, y):
    return x**2 + 3*x*y + y**3

def partial_dev():
    x,y = symbols('x y')
    f = (2*x**3)+ (3*y**3)
    df_dx = diff(f,x)
    df_dy = diff(f,y)
    print(df_dx)
    print(df_dy)
    plot3d(f)

if __name__ == "__main__":
   partial_dev()