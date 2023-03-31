
import pandas as pd

class CrossTab_Item4:
    
    def __init__(self, dataframe, column):
        self.df_item4 = dataframe.copy()
        self.column = column
        self.days_map = {1 : 'Sunday', 2 : 'Monday', 3 : 'Tuesday', 4 : 'Wednesday',
                         5 : 'Thursday', 6 : 'Friday', 7 : 'Saturday'}
        self.item4_crosstab()
    
    def item4_crosstab(self):
        
        # Applying changes
        self.df_item4[self.column] = self.df_item4[self.column].map(self.days_map)
        
        # Showing crosstab
        self.crosstab_Q4 = pd.crosstab(self.df_item4[self.column], self.df_item4['converted'], normalize = 'index') \
                             .apply(lambda x: round((x * 100), 2)) \
                             .applymap('{:.2f}%'.format).sort_values(by = 1, ascending = False)
        
        return

