
from scipy.stats import chi2_contingency
import numpy as np

def chi2_test(dataframe, grupos, convertidos):
    
    # Number of clients which seen private advertisement, split by conversion
    converted_private = len(dataframe[(dataframe[grupos] == 1) & (dataframe[convertidos] == 1)])
    not_converted_private = len(dataframe[(dataframe[grupos] == 1) & (dataframe[convertidos] == 0)])
    
    # Number of clients which seen public advertisement, split by conversion
    converted_public = len(dataframe[(dataframe[grupos] == 0) & (dataframe[convertidos] == 1)])
    not_converted_public = len(dataframe[(dataframe[grupos] == 0) & (dataframe[convertidos] == 0)])
    
    # Number of observations split by clients which seen private or public advertisement
    n_private = converted_private + not_converted_private
    n_public = converted_public + not_converted_public
    
    # Proportion of clientes converted in each group
    prop_private = converted_private / n_private
    prop_public = converted_public / n_public

    # Contingency table of the observed frequencies of conversions in each group
    observed = np.array([[converted_private, n_private - converted_private],
                         [converted_public, n_public - converted_public]])

    # Perform a chi-squared test of independence
    chi2_stat, p_value, dof, expected = chi2_contingency(observed)

    # Print the results
    print(f'Proportion of converted within clients which seen private advertisement: {prop_private:.2%}')
    print(f'Proportion of converted within clients which seen public advertisement: {prop_public:.2%}')
    
    if p_value < 0.05:
        print(f'P-value = {p_value:.6f}! We can reject the null hypothesis. There is a significant difference between the proportions!')
    else:
        print(f'P-value = {p_value:.6f}!) We can not reject the null hypothesis. There is no significante difference between the proportions!')

