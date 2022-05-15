import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

csv_file = 'https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/uci-heart-disease/heart.csv'
df = pd.read_csv(csv_file)

def prob_density_func(n, mean, std):
  reg = 1 / (std * np.sqrt(2 * 3.14))
  expo = np.exp(-1 * (n - mean) ** 2 / (2 * std ** 2))
  return reg * expo

cholestrol_not_having_disease = df[df['target'] == 0]['chol']
my_mean = cholestrol_not_having_disease.mean()
my_std = cholestrol_not_having_disease = df[df['target'] == 0]['chol'].std()
my_min = cholestrol_not_having_disease.min()
my_max = cholestrol_not_having_disease.max()
sorted_vals = cholestrol_not_having_disease.sort_values()
prob_values = prob_density_func(sorted_vals, my_mean, my_std)

# calculate the z-score for the cholesterol levels 
z_score_150 = (150 - my_mean) / my_std
z_score_200 = (200 - my_mean) / my_std

def area_filled_min_to_200_probability_density_distribution():
    my_array = np.arange(my_min, 201)
    area_vals = prob_density_func(my_array, my_mean, my_std)
    plt.figure(figsize = (20, 10))
    plt.plot(sorted_vals, prob_values)
    plt.fill_between(x = np.arange(my_min, 201), y1 = area_vals, facecolor = 'yellow', alpha = 0.5)
    plt.axvline(x = 200, label = '200', color = 'blue')
    plt.xlabel('probablity density')
    plt.ylabel('probability')
    plt.legend()
    plt.show()

    # use cumulative distribution function to find the probability of patients not having heart disease having cholesterol level <= 200
    # cdf will use the z scores because it is uniform and normalized
    probability = norm.cdf(z_score_200)
    print(probability)

def area_filled_min_to_200_probability_density_distribution():
    my_array = np.arange(my_min, 151)
    area_vals = prob_density_func(my_array, my_mean, my_std)
    plt.figure(figsize = (20, 10))
    plt.plot(sorted_vals, prob_values)
    plt.fill_between(x = np.arange(my_min, 151), y1 = area_vals, facecolor = 'yellow', alpha = 0.5)
    plt.axvline(x = 150, label = '150', color = 'blue')
    plt.xlabel('probablity density')
    plt.ylabel('probability')
    plt.legend()
    plt.show()

    # calc probability again
    print(norm.cdf(z_score_150))

def area_filled_200_to_max_probability_density_distribution():
    my_array = np.arange(200, my_max)
    area_vals = prob_density_func(my_array, my_mean, my_mean)
    plt.figure(figsize = (20, 10))
    plt.plot(sorted_vals(), prob_values)
    plt.fill_between(x = np.arange(200, my_max), y1 = area_vals, facecolor = 'yellow', alpha = 0.5)
    plt.axvline(x = 200, label = '200', color = 'blue')
    plt.xlabel('probablity density')
    plt.ylabel('probability')
    plt.legend()
    plt.show()

    # calc probability
    print(1 - norm.cdf(z_score_200))

def area_filled_150_200_probability_density_distribution():
    
    area_vals = prob_density_func(np.arange(150, 201), my_mean, my_std)
    plt.figure(figsize = (20, 10))
    plt.plot(sorted_vals, prob_values)
    plt.fill_between(x = np.arange(150, 201), y1 = area_vals, facecolor = 'yellow', alpha = 0.5)
    plt.axvline(150, label = '150', color = 'red', linestyle = '--')
    plt.axvline(x = 200, label = '200', color = 'blue')
    plt.xlabel('probablity density')
    plt.ylabel('probability')
    plt.legend()
    plt.show()

    # probabilty is 1 - (p(chol <= 150) + p(chol > 200))
    # = 1 - (cdf(z_score_150) + (1 - cdf(z_score_200)))
    # = = 1 - cdf(z_score_150) - (1 - cdf(z_score_200))
    # = 1 - cdf(z_score_150) - 1 + cdf(z_score_200)
    # = cdf(z_score_200) - cdf(z_score_150)
    print(norm.cdf(z_score_200) - norm.cdf(z_score_150))