
from scipy.stats import mannwhitneyu

def MW_test(dataframe, column):

    # Mann-Whitney test
    converted = dataframe[dataframe['converted'] == 1][column]
    non_converted = dataframe[dataframe['converted'] == 0][column]

    result = mannwhitneyu(converted, non_converted)

    return print('p-value:', result.pvalue)
