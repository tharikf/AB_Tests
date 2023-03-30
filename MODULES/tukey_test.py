

from statsmodels.stats.multicomp import pairwise_tukeyhsd

def tukey_test(dataframe, target_variable, independent_variable):
    
    # Perform Tukey's HSD test with Bonferroni correction
    tukey_results = pairwise_tukeyhsd(dataframe[target_variable], dataframe[independent_variable])
    
    # Printing results
    print(tukey_results)
    
    #return cross_df

