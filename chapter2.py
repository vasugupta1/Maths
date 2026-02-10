from collections import defaultdict
from math import sqrt
from matplotlib.pylab import norm
import scipy.stats as  stats
import pandas as pd
import matplotlib.pyplot as plt
import random as rd 
import numpy as np
from scipy.stats import norm

def start_probability():
   p_coffe_drinker = 0.65
   p_cacner = 0.005
   p_coffe_drinker_given_cancer = 0.85
   
   p_cancer_given_coffe_drinker = (p_coffe_drinker_given_cancer*p_cacner)/p_coffe_drinker
   print(p_cancer_given_coffe_drinker*100)


def mean():
   sample = [1,2,3,4,5,6,7,9,10]
   mean = sum(sample)/ len(sample)
   print(mean)

def weighted_mean():
   sample = [90,80,63,87]
   weights = [0.20, 0.20, 0.20, 0.40]
   weighted_sum = sum((s*w  for  s,w in zip(sample, weights))) / sum(weights)
   print(weighted_sum)


def median():
   sample = [0, 1,5,7,9,10,14]
   ordered_sample = sorted(sample)
   n = len(sample)
   if n % 2 == 0 :
      mid = n /2 
      print(ordered_sample[mid])
   else:
     mid = int(n / 2) - 1 
     result = (ordered_sample[mid] + ordered_sample[mid+1] ) / 2 
     print(result)

def mode():
   sample = [0, 1,5,7,9,10,14, 14]
   count = defaultdict(lambda: 0)
   for s in sample:
      count[s] += 1
   
   max_count = max(count.values())
   mode = [v for v in set(count) if count[v] == max_count]
   print(mode)

def varaince():
   sample = [0, 1,5,7,9,10,14]
   n = len(sample)
   mean = sum(sample) / n
   result = 0
   for _ ,v in enumerate(sample):
      result += (v - mean)**2
   print(result / n)

def another_way_of_varaince():
   sample = [0, 1,5,7,9,10,14]
   n = len(sample)
   mean = sum(sample) / n
   var = sum((v- mean)**2 for v in sample)/n
   print(var)

def std(is_sample: bool = False):
   sample = [0, 1,5,7,9,10,14]
   n = len(sample)
   mean = sum(sample) / n
   var = sum((v- mean)**2 for v in sample)/ (n -1 if is_sample else n)
   std = sqrt(var)
   print(std)

def uniform_distribtions():
   uniform_data = stats.uniform.rvs(size= 100_000, loc= 0, scale= 10)
   pd.DataFrame(uniform_data).plot(kind= "density")
   plt.show()

def random_int():
   print(rd.choice([2,4,6,8]))
   print(rd.uniform(0,10))

# this makes sure that the random number I do produce are going to be the same random num each time
def random_with_seed():
   rd.seed(12)
   print([rd.uniform(0,10) for x in range(4)])
   rd.seed(12)
   print([rd.uniform(0,10) for x in range(4)])
   rd.seed(13)
   print([rd.uniform(0,10) for x in range(4)])

def normal_dis():
   prob_under_minus_one = stats.norm.cdf(x = -1, loc = 0, scale = 1)
   print(prob_under_minus_one)
   prob_over_one = stats.norm.cdf(x = 1 , loc = 0, scale = 1)
   print(prob_over_one)
   between_prob = 1 - (prob_over_one + prob_under_minus_one)
   print(between_prob)


def plot_normal_dis():
   plt.rcParams["figure.figsize"] = (7,7)
   x = np.arange(-4, 4, 0.01)
   plt.fill_between(x = x, y1 = stats.norm.pdf(x = x))
   plt.show()
   print(stats.norm.pdf(x = 0))



def normal_dis_cdf():
   mean = 64.43
   std = 2.99
   x = norm.cdf(x = mean, loc = mean, scale = std)
   print(x)


def z_scores(x, mean,std):
   z = (x - mean ) / std;
   return z

def compare_2_houses():
   first_house_z_score = z_scores(x = 150_000, mean = 140_000, std = 3000)
   second_house_z_score = z_scores(x = 800_000, mean = 800_000, std = 10_000)

   if abs(first_house_z_score) < abs(second_house_z_score):
      print("first house is better")
   elif abs(first_house_z_score) > abs(second_house_z_score):
      print("second house is better")
   else:      print("both are equally good")



if __name__ == "__main__":
   z_scores(x = 67.42, mean = 64.43, std = 2.99)
   compare_2_houses()
   