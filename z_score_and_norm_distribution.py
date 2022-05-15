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

# data for cholesterol in people with no heart disease follows normal distribution
def cholesterol_no_heart_disease_distribution():
    plt.figure(figsize = (20, 10))
    sns.distplot(cholesterol_not_having_disease, bins = 'sturges', hist = False)
    plt.title('cholesterol in people who do not have heart disease', fontsize = 20)
    plt.xlabel('cholesterol', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(cholesterol_not_having_disease.mean(), label = str(round(cholesterol_not_having_disease.mean(), 2)), color = 'red')
    plt.legend()
    plt.show()

# plot normalized data (using z scores)

# follows normal distribution like non-normalized dataset
def z_scores_cholesterol_no_heart_disease_distribution():
    
    cholesterol_not_having_disease = df[df['target'] == 0]['chol']
    my_mean = cholesterol_not_having_disease.mean()
    my_std = cholesterol_not_having_disease.std()
    my_series = pd.Series([(i - my_mean) / my_std for i in cholesterol_not_having_disease])
    plt.figure(figsize = (20, 10))
    sns.distplot(my_series, bins = 'sturges', hist = False)
    plt.title('z score for cholesterol in people who do not have heart disease', fontsize = 20)
    plt.xlabel('z values', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(my_series.mean(), label = str(round(my_series.mean(), 2)), color = 'red')
    plt.legend()
    plt.show()

cholesterol_having_disease = df[df['target'] == 1]['chol']

# data for cholesterol in people with heart disease does not follow normal distribution
def cholesterol_no_heart_disease_distribution():
    plt.figure(figsize = (20, 10))
    sns.distplot(cholesterol_having_disease, bins = 'sturges', hist = False)
    plt.title('cholesterol in people who have heart disease', fontsize = 20)
    plt.xlabel('cholesterol', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(cholesterol_having_disease.mean(), label = str(round(cholesterol_having_disease.mean(), 2)), color = 'red')
    plt.legend()
    plt.show()

# plot normalized data (using z scores)

# z scores do not follow normal distribution because non-normalized dataset also does not follow it
def z_scores_cholesterol_with_heart_disease_distribution():
  
    my_mean = cholesterol_having_disease.mean()
    my_std = cholesterol_having_disease.std()
    my_series = pd.Series([(i - my_mean) / my_std for i in cholesterol_having_disease])
    plt.figure(figsize = (20, 10))
    sns.distplot(my_series, bins = 'sturges', hist = False)
    plt.title('z scores for cholesterol in people who have heart disease', fontsize = 20)
    plt.xlabel('z values', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(my_series.mean(), label = str(round(my_series.mean(), 2)), color = 'red')
    plt.legend()
    plt.show()

