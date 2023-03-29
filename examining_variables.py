
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import kstest

# Visualization of continuous variable
def continuous_viz(dataframe, coluna):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 8))

    # Create kernel density plot
    ax1 = sns.kdeplot(data=dataframe, x=coluna, ax = ax1)

    # Create Q-Q plot
    ax2 = sm.qqplot(dataframe[coluna], fit = True, line = 's', ax = ax2)

    # Show plots
    return plt.show()


# Kolmogorov-Smirnov test of normality in very large samples
def KS_test(dataframe, coluna):

    # Shapiro-Wilk test
    stat, p = kstest(dataframe[coluna], 'norm')

    # Alpha value
    alpha = 0.05

    if p > 0.05:
        print(f'Fail to reject H0! Evidence of normality! p-value = {p}')
    else:
        print(f'Reject H0! No evidence of normality! p-value = {p}')

    return

