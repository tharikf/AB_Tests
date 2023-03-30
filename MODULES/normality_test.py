
from scipy.stats import kstest


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
