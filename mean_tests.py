
from scipy.stats import mannwhitneyu

def MW_test(dataframe, coluna):

    # Mann-Whitney test
    converted = dataframe[dataframe['converted'] == 1][coluna]
    non_converted = dataframe[dataframe['converted'] == 0][coluna]

    resultado = mannwhitneyu(converted, non_converted)

    return print('Valor p:', resultado.pvalue)
