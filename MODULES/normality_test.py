
from scipy.stats import kstest


def KS_test(dataframe, column):

    # Kolmogorov-Smirnov test
    stat, p = kstest(dataframe[column], 'norm')

    # Alpha value
    alpha = 0.05

    if p > alpha:
        return print(f'Fail to reject H0! Evidence of normality! p-value = {p}')
    else:
        return print(f'Reject H0! No evidence of normality! p-value = {p}')

