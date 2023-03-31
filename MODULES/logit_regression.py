import statsmodels.api as sm
import pandas as pd

def logit_transformation(dataframe):
    
    # Copying dataframe
    df_logit = dataframe.copy()
    
    # Applying changes
    groups_map = {0 : 'Public_Ad', 1 : 'Private_Ad'}
    days_map = {1 : 'Sunday', 2 : 'Monday', 3 : 'Tuesday', 4 : 'Wednesday', 5 : 'Thursday', 6 : 'Friday', 7 : 'Saturday'}
    hours_map = {0 : 'Early Morning', 1 : 'Morning', 2 : 'Afternoon', 3 : 'Evening'}
    
    df_logit['groups'] = df_logit['groups'].map(groups_map)
    df_logit['most_ads_day'] = df_logit['most_ads_day'].map(days_map)
    df_logit['most_ads_hour'] = df_logit['most_ads_hour'].map(hours_map)
    
    # Get dummies
    groups_dummies = pd.get_dummies(df_logit['groups'])
    day_dummies = pd.get_dummies(df_logit['most_ads_day'])
    hour_dummies = pd.get_dummies(df_logit['most_ads_hour'])
    
    # Concat
    df_logit = pd.concat([df_logit[['converted', 'total_ads']], groups_dummies, day_dummies, hour_dummies], axis = 1)
    
    # Getting the dependent variable
    y = df_logit.iloc[:, 0]
    
    # Getting the independent variables
    '''
    It's worth noting that when creating dummies from a categorical variable for use in logistic regression,
    we must drop at least one dummy column to serve as our reference point. For example, suppose we're creating
    dummies to indicate the period of the day when the client views advertisements the most. We might include
    Early Morning, Morning, and Evening dummies while omitting Afternoon. We do this to use Afternoon as our
    reference point, so the results of these dummies can be compared to Afternoon. This practice is applied to
    other dummies as well when using the logit algorithm to avoid convergence problems.
    '''
    X = df_logit.loc[:, ['total_ads', 'Public_Ad', 'Early Morning', 'Morning', 'Evening',
                         'Tuesday', 'Wednesday', 'Sunday', 'Friday', 'Thursday', 'Saturday']]
    
    # Fitting logistic regression
    logit = sm.Logit(y, sm.add_constant(X)).fit()
    
    return logit.summary()

