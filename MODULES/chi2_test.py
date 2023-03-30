
from scipy.stats import chi2_contingency
import numpy as np

def chi2_test(dataframe, converted_column, variable_investigated, group1, group2):
    
    # The variable investigated is split by conversion, showing the number of clients in group 1
    converted_gp1 = len(dataframe[(dataframe[variable_investigated] == group1) & (dataframe[converted_column] == 1)])
    not_converted_gp1 = len(dataframe[(dataframe[variable_investigated] == group1) & (dataframe[converted_column] == 0)])
    
    # The variable investigated is split by conversion, showing the number of clients in group 2
    converted_gp2 = len(dataframe[(dataframe[variable_investigated] == group2) & (dataframe[converted_column] == 1)])
    not_converted_gp2 = len(dataframe[(dataframe[variable_investigated] == group2) & (dataframe[converted_column] == 0)])
    
    # Total observations in each group
    n_gp1 = converted_gp1 + not_converted_gp1
    n_gp2 = converted_gp2 + not_converted_gp2
    
    # Proportion of clientes converted in each group
    prop_gp1 = converted_gp1 / n_gp1
    prop_gp2 = converted_gp2 / n_gp2

    # Contingency table of the observed frequencies of conversions in each group
    observed = np.array([[converted_gp1, n_gp1 - converted_gp1],
                         [converted_gp2, n_gp2 - converted_gp2]])

    # Perform a chi-squared test of independence
    chi2_stat, p_value, dof, expected = chi2_contingency(observed)

    # Print the results
    print(f'Proportion of converted within clients in group one: {prop_gp1:.2%}')
    print(f'Proportion of converted within clients in group two: {prop_gp2:.2%}')
    
    if p_value < 0.05:
        print(f'P-value = {p_value:.6f}! We can reject the null hypothesis. There is a significant difference between the proportions!')
    else:
        print(f'P-value = {p_value:.6f}!) We can not reject the null hypothesis. There is no significante difference between the proportions!')
    

