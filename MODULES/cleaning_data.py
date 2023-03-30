

import pandas as pd
import numpy as np

def cleaning_data(dataframe):
    
    # Droping the index column
    dataframe = dataframe.drop(columns = ['Unnamed: 0', 'user id'])
    
    # Rename columns
    dataframe.columns = ['groups', 'converted', 'total_ads', 'most_ads_day', 'most_ads_hour']
    
    # Changing variables in groups column (Private Ad = 1, Public Ad = 0)
    dataframe['groups'] = np.where(dataframe['groups'] == 'ad', 1, 0)
    
    # Changing variables in converted column (True = 1, False = 0)
    dataframe['converted'] = np.where(dataframe['converted'] == True, 1, 0)
    
    # Changing variables in most_ads_day column
    days_map = {'Sunday' : 1, 'Monday' : 2, 'Tuesday' : 3, 'Wednesday' : 4, 'Thursday' : 5, 'Friday' : 6, 'Saturday' : 7}
    dataframe['most_ads_day'] = dataframe['most_ads_day'].map(days_map)

    # Changing variables in most_ads_hour
    # 0 = Dawn, 1 = Morning, 2 = Afternoon, 3 = Nigh
    dataframe['most_ads_hour'] = np.where((dataframe['most_ads_hour'] >= 0) & (dataframe['most_ads_hour'] <= 5), 0,
                                    np.where((dataframe['most_ads_hour'] >= 6) & (dataframe['most_ads_hour'] <= 11), 1,
                                         np.where((dataframe['most_ads_hour'] >= 12) & (dataframe['most_ads_hour'] <= 17), 2, 3)))
    
    return dataframe