import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = 'https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/uci-heart-disease/heart.csv'
df = pd.read_csv(csv_file)

def cholesterol_vs_presense_of_heart_disease_boxplot():
    plt.figure(figsize = (20, 10))
    sns.boxplot(x = 'chol', y = 'target', data = df, orient = 'h')
    plt.show()

cholesterol_not_having_disease = df[df['target'] == 0]['chol']
not_having_mean = cholesterol_not_having_disease.mean()
not_having_std = cholesterol_not_having_disease.std()

# data for cholesterol in people with no heart disease follows normal distribution
def cholesterol_no_heart_disease_distribution():
    plt.figure(figsize = (20, 10))
    sns.distplot(cholesterol_not_having_disease, bins = 'sturges', hist = False)
    plt.title('cholesterol in people who do not have heart disease', fontsize = 20)
    plt.xlabel('cholesterol', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(not_having_mean, label = str(round(not_having_mean, 2)), color = 'red')
    plt.legend()
    plt.show()

# plot normalized data (using z scores)

# follows normal distribution like non-normalized dataset
def z_scores_cholesterol_no_heart_disease_distribution():
    

    my_series = pd.Series([(i - not_having_mean) / my_std for i in cholesterol_not_having_disease])
    series_mean = my_series.mean()
    plt.figure(figsize = (20, 10))
    sns.distplot(my_series, bins = 'sturges', hist = False)
    plt.title('z score for cholesterol in people who do not have heart disease', fontsize = 20)
    plt.xlabel('z values', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(series_mean, label = str(round(series_mean, 2)), color = 'red')
    plt.legend()
    plt.show()

cholesterol_having_disease = df[df['target'] == 1]['chol']
having_mean = cholesterol_having_disease.mean()
having_std = cholesterol_having_disease.std()

# data for cholesterol in people with heart disease does not follow normal distribution
def cholesterol_no_heart_disease_distribution():
    plt.figure(figsize = (20, 10))
    sns.distplot(cholesterol_having_disease, bins = 'sturges', hist = False)
    plt.title('cholesterol in people who have heart disease', fontsize = 20)
    plt.xlabel('cholesterol', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(having_mean, label = str(round(having_mean, 2)), color = 'red')
    plt.legend()
    plt.show()

# plot normalized data (using z scores)

# z scores do not follow normal distribution because non-normalized dataset also does not follow it
def z_scores_cholesterol_with_heart_disease_distribution():
  
    
    my_series = pd.Series([(i - having_mean) / having_std for i in cholesterol_having_disease])
    series_mean = my_series.mean()
    plt.figure(figsize = (20, 10))
    sns.distplot(my_series, bins = 'sturges', hist = False)
    plt.title('z scores for cholesterol in people who have heart disease', fontsize = 20)
    plt.xlabel('z values', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(series_mean, label = str(round(series_mean, 2)), color = 'red')
    plt.legend()
    plt.show()

