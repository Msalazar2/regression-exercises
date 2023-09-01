import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import wrangle as w
import prepare as p
from scipy import stats


def plot_variable_pairs(df):
    
    sns.set(style="ticks")
    sns.pairplot(df.sample(5_000), kind ="reg", corner = True)
    plt.show()



def plot_categorical_and_continuous_vars(df, categorical, continuous):

    plt.figure(figsize=(15, 5))

    # Boxplot
    plt.subplot(1, 3, 1)
    sns.boxplot(x = categorical, y = continuous, data = df.sample(5_000))
    plt.title("Boxplot")

    # Scatterplot
    plt.subplot(1, 3, 2)
    sns.scatterplot(x = categorical, y = continuous, data = df.sample(5_000))
    plt.title("Scatterplot")

    # Barplot
    plt.subplot(1, 3, 3)
    sns.barplot(x = categorical, y = continuous, data = df.sample(5_000))
    plt.title("Barplot")

    plt.tight_layout()
    plt.show()
    
    
    
def spear_test(df, continuous, continuous2):
    
    r, p = stats.spearmanr(df[continuous], df[continuous2])

    print(f'r = {r}')
    print(f'p = {p}')
    
    print('')
    
    a = .05

    if p < a:

        print('Conclusion: Reject the null, There is a correlation')

    else:

        print('Conclusion: Fail to reject the null, There is not a correlation')