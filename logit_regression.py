
import statsmodels.api as sm

def logistic_regression(dataframe):

    # Implementing logistic regression
    logit = sm.Logit(dataframe['converted'], dataframe[['groups', 'total_ads', 'most_ads_day', 'most_ads_hour']]).fit()

    # Print results
    
    return print(logit.summary())