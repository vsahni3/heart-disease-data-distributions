import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/uci-heart-disease/heart.csv')

# show that the data follows central limit theorem
def general_cholesterol_visualization():
    plt.figure(figsize = [20, 10])
    plt.hist(df['chol'], bins = 'sturges')
    plt.xlabel('Patient Number')
    plt.ylabel('Patient cholesterol')
    plt.axvline(df['chol'].mean(), label = str(df['chol'].mean()), color = 'red')
    plt.title('Cholesterol Observations')
    plt.legend()
    plt.show()

def cholesterol_random_medium_sample_mean_visualization():
    my_list = [df['chol'].sample(n = 30).mean() for i in range(300)]
    plt.figure(figsize = [20, 10])
    plt.hist(my_list, bins = 'sturges')
    plt.xlabel('Mean cholesterol')
    plt.ylabel('Frequency')
    plt.axvline(pd.Series(my_list).mean(), label = str(pd.Series(my_list).mean()), color = 'red')
    plt.title('cholesterol Observations')
    plt.legend()
    plt.show()

def cholesterol_random_many_large_samples_mean_visualization():
    first = [df['chol'].sample(n = 500, replace = True).mean() for i in range(300)]
    second = [df['chol'].sample(n = 1000, replace = True).mean() for i in range(300)]
    third = [df['chol'].sample(n = 10000, replace = True).mean() for i in range(300)]

    plt.figure(figsize = [20, 10])
    sns.distplot(first, bins = 'sturges', hist = False, label = '500')
    sns.distplot(second, bins = 'sturges', hist = False, label = '1000')
    sns.distplot(third, bins = 'sturges', hist = False, label = '10000')
    plt.xlabel('Mean cholesterol')
    plt.ylabel('Frequency')
    plt.title('cholesterol Observations')
    plt.legend()
    plt.show()

    print(pd.Series(first).mean())
    print(pd.Series(second).mean())
    print(np.mean(third))

def cholesterol_random_small_sample_mean_visualization():
    my_list = [df['chol'].sample(n = 2).mean() for i in range(10000)]
    plt.figure(figsize = [20, 10])
    sns.distplot(my_list, bins = 'sturges', hist = False)
    plt.xlabel('Mean cholesterol')
    plt.ylabel('Frequency')
    plt.axvline(pd.Series(my_list).mean(), label = str(pd.Series(my_list).mean()), color = 'red')
    plt.title('cholesterol Observations')
    plt.legend()
    plt.show()

def general_blood_pressure_visualization():
    plt.figure(figsize = (20, 10))
    plt.hist(df['trestbps'], bins = 'sturges')
    plt.xlabel('Blood Pressure')
    plt.ylabel('Frequency')
    plt.axvline(pd.Series(df['trestbps']).mean(), label = str(df['trestbps'].mean()), color = 'red')
    plt.title('Blood Pressure Observations')
    plt.legend()
    plt.show()

def blood_pressure_random_medium_sample_mean_visualization():
    my_list = [df['trestbps'].sample(n = 30).mean() for i in range(500)]
    plt.figure(figsize = [20, 10])
    sns.distplot(my_list, bins = 'sturges', hist = False)
    plt.xlabel('Mean Blood Pressure')
    plt.ylabel('Frequency')
    plt.axvline(pd.Series(my_list).mean(), label = str(pd.Series(my_list).mean()), color = 'red')
    plt.title('Mean Blood Pressure Observations')
    plt.legend()
    plt.show()

def general_heart_rate_visualization():
    plt.figure(figsize = (20, 10))
    plt.hist(df['thalach'], bins = 'sturges')
    plt.xlabel('Heart Rate')
    plt.ylabel('Frequency')
    plt.axvline(pd.Series(df['thalach']).mean(), label = str(df['thalach'].mean()), color = 'red')
    plt.title('Heart Rate Observations')
    plt.legend()
    plt.show()

def heart_rate_random_medium_sample_mean_visualization():
    my_list = [df['thalach'].sample(n = 30).mean() for i in range(1000)]
    plt.figure(figsize = [20, 10])
    sns.distplot(my_list, bins = 'sturges', hist = False)
    plt.xlabel('Mean Heart Rate')
    plt.ylabel('Frequency')
    plt.axvline(pd.Series(my_list).mean(), label = str(pd.Series(my_list).mean()), color = 'red')
    plt.title('Mean Heart Rate Observations')
    plt.legend()
    plt.show()