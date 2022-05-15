import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = 'https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/uci-heart-disease/heart.csv'
df = pd.read_csv(csv_file)

def cholestrol_vs_presense_of_heart_disease_boxplot():
    plt.figure(figsize = (20, 10))
    sns.boxplot(x = 'chol', y = 'target', data = df, orient = 'h')
    plt.show()

cholestrol_not_having_disease = df[df['target'] == 0]['chol']

# data for cholestrol in people with no heart disease follows normal distribution
def cholestrol_no_heart_disease_distribution():
    plt.figure(figsize = (20, 10))
    sns.distplot(cholestrol_not_having_disease, bins = 'sturges', hist = False)
    plt.title('cholestrol in people who do not have heart disease', fontsize = 20)
    plt.xlabel('cholestrol', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(cholestrol_not_having_disease.mean(), label = str(round(cholestrol_not_having_disease.mean(), 2)), color = 'red')
    plt.legend()
    plt.show()

# plot normalized data (using z scores)

# follows normal distribution like non-normalized dataset
def z_scores_cholestrol_no_heart_disease_distribution():
    
    cholestrol_not_having_disease = df[df['target'] == 0]['chol']
    my_mean = cholestrol_not_having_disease.mean()
    my_std = cholestrol_not_having_disease.std()
    my_series = pd.Series([(i - my_mean) / my_std for i in cholestrol_not_having_disease])
    plt.figure(figsize = (20, 10))
    sns.distplot(my_series, bins = 'sturges', hist = False)
    plt.title('z score for cholestrol in people who do not have heart disease', fontsize = 20)
    plt.xlabel('z values', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(my_series.mean(), label = str(round(my_series.mean(), 2)), color = 'red')
    plt.legend()
    plt.show()

cholestrol_having_disease = df[df['target'] == 1]['chol']

# data for cholestrol in people with heart disease does not follow normal distribution
def cholestrol_no_heart_disease_distribution():
    plt.figure(figsize = (20, 10))
    sns.distplot(cholestrol_having_disease, bins = 'sturges', hist = False)
    plt.title('cholestrol in people who have heart disease', fontsize = 20)
    plt.xlabel('cholestrol', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(cholestrol_having_disease.mean(), label = str(round(cholestrol_having_disease.mean(), 2)), color = 'red')
    plt.legend()
    plt.show()

# plot normalized data (using z scores)

# z scores do not follow normal distribution because non-normalized dataset also does not follow it
def z_scores_cholestrol_with_heart_disease_distribution():
  
    my_mean = cholestrol_having_disease.mean()
    my_std = cholestrol_having_disease.std()
    my_series = pd.Series([(i - my_mean) / my_std for i in cholestrol_having_disease])
    plt.figure(figsize = (20, 10))
    sns.distplot(my_series, bins = 'sturges', hist = False)
    plt.title('z scores for cholestrol in people who have heart disease', fontsize = 20)
    plt.xlabel('z values', fontsize = 15)
    plt.ylabel('probability', fontsize = 15)
    plt.axvline(my_series.mean(), label = str(round(my_series.mean(), 2)), color = 'red')
    plt.legend()
    plt.show()

