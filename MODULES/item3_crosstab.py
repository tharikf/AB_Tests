
import pandas as pd


class CrossTab_Item3:
    
    def __init__(self, dataframe, column):
        self.df_item3 = dataframe.copy()
        self.column = column
        self.hours_map = {0 : 'Early Morning', 1 : 'Morning', 2 : 'Afternoon', 3 : 'Evening'}
        self.item3_crosstab()
        
    def item3_crosstab(self):
        
        #Applying changes
        self.df_item3[self.column] = self.df_item3[self.column].map(self.hours_map)
        
        # Creating Crosstab
        self.crosstab_Q3 = pd.crosstab(self.df_item3[self.column], self.df_item3['converted'], normalize = 'index') \
                             .apply(lambda x: round((x * 100), 2)) \
                             .applymap('{:.2f}%'.format).sort_values(by = 1, ascending = False)
        
        return
