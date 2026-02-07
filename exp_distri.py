from collections import defaultdict
from math import sqrt
import scipy.stats as  stats
import pandas as pd
import matplotlib.pyplot as plt
import random as rd 
import numpy as np


def create_exp_data(mean: float):
    exp_lamda = 1 / mean
    scale = 1 / exp_lamda
    return stats.expon(scale = scale)

def plot_exp(mean: float) -> list[float]:
   data = stats.expon.rvs(scale=mean, size=1000)
   print(data)
   df = pd.DataFrame(data, columns=['Exponential Data'])
   df.plot(kind="density")
   plt.show()
   return data

# def cal_prob(x: float, ):


if __name__ == "__main__":
    plot_exp(5)